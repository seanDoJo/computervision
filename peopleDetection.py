import cv2

def selectPeople(files):
    people = []
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    for filen in files:
        im = cv2.imread(filen)
        im = cv2.resize(im, (im.shape[0],min(400, im.shape[1])))

        (locations, weights) = hog.detectMultiScale(im, winStride=(4, 4), padding=(8, 8), scale=1.05)

        if len(locations) >= 1:
            people.append(filen)
    return people
