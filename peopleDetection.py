"""

Authors: Sean Donohoe, Kyle Wiese
CSCI 5722 Final Project

"""

import cv2

def selectPeople(files):
    people = []
    hog = cv2.HOGDescriptor()
    # get the HOG people detector
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    for filen in files:
        # following along with the tutorial at: http://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/

        im = cv2.imread(filen)
        im = cv2.resize(im, (im.shape[0] ,min(400, im.shape[1])))

        (locations, weights) = hog.detectMultiScale(im, winStride=(4, 4), padding=(8, 8), scale=1.05)
        
        # only return images in which there are people
        if len(locations) >= 1:
            people.append(filen)
    return people

def fit(im):
    if (im.shape[0]*im.shape[1]) > 250000:
        s = max(im.shape[0], im.shape[1])
        s = 1/float(s / 500)
        im = cv2.resize(im, (0, 0), fx=s, fy=s)
    return im

def clusterPeople(files):
    fileLabels = {}
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    sift = cv2.xfeatures2d.SIFT_create()
    matcher = cv2.BFMatcher()

    # Extract all images with faces, keeping track of the face sub-images for each photo
    for filen in files:
        im = cv2.imread(filen)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(im, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        if len(faces) >= 1:
            fileLabels[filen] = []

            for (x, y, w, h) in faces:
                fileLabels[filen].append(im[y:y+h, x:x+w])
    
    # Compute SIFT feature descriptors for each face
    features = [
        (filename, sift.detectAndCompute(fit(image), None)[1]) for filename in fileLabels
        for image in fileLabels[filename]
    ]
    clusters = {filename: [] for filename in fileLabels}

    nums = len(features)
    for i in range(0, nums):
        pdes = features[i][1]
        for j in range(0, nums):
            if j == i or features[i][0] == features[j][0]:
                continue
            sdes = features[j][1]
            gcount = 0

            # calculate the 2 nearest neighbors and apply the ratio test
            loweMatches = matcher.knnMatch(pdes, sdes, k=2)
            if len(loweMatches) >= 2:
                for m1, m2 in loweMatches:
                    if m1.distance < 0.75*m2.distance and m1.distance <= 300:
                        gcount += 1

                # cluster the two images if the faces match
                if gcount >= 10:
                    clusters[features[i][0]].append(
                        features[j][0]
                    )
    for k in clusters:
        clusters[k] = set(clusters[k])
    return clusters
