import cv2

def selectPeople(files):
    people = []
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    for filen in files:
        im = cv2.imread(filen)
        im = cv2.resize(im, (im.shape[0],min(400, im.shape[1])))

        (locations, weights) = hog.detectMultiScale(im, winStride=(4, 4), padding=(8, 8), scale=1.1)

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

    for filen in files:
        im = cv2.imread(filen)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(im, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        if len(faces) >= 1:
            fileLabels[filen] = []

            for (x, y, w, h) in faces:
                fileLabels[filen].append(im[y:y+h, x:x+w])

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
            needed = max(int(0.1*min(len(pdes), len(sdes))), 10)
            gcount = 0
            loweMatches = matcher.knnMatch(pdes, sdes, k=2)
            for m1, m2 in loweMatches:
                if m1.distance < 0.75*m2.distance and m1.distance <= 300:
                    gcount += 1
            if gcount >= 10:
                clusters[features[i][0]].append(
                    features[j][0]
                )
    return clusters
