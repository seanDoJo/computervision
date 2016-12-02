"""

Authors: Sean Donohoe, Kyle Wiese
CSCI 5722 Final Project

"""

import numpy as np
import cv2
import os
import gc

def fit(filename):
	im = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2GRAY)
	
	if (im.shape[0]*im.shape[1]) > 250000:
		s = max(im.shape[0], im.shape[1])
		s = 1/float(s / 500)
		im = cv2.resize(im, (0, 0), fx=s, fy=s)
	
	return im

def clusterPhotos(files):
    sift = cv2.xfeatures2d.SIFT_create()
    matcher = cv2.BFMatcher()

    visited = {k: False for k in files}
    clusters = {filename: [] for filename in files}

    # Extract sift feature descriptors and pair with the filename
    features = [
            (filename, sift.detectAndCompute(fit(filename), None)[1]) for filename in files
    ]
    nums = len(features)
    for i in range(0, nums):
            pdes = features[i][1]
            for j in range(0, nums):
                    if j == i:
                            continue
                    sdes = features[j][1]
                    gcount = 0
                    
                    # calculate the 2 nearest neighbors for each feature
                    loweMatches = matcher.knnMatch(pdes, sdes, k=2)
                    for m1, m2 in loweMatches:
                            # only accept the feature if it passes the ratio test and is within a threshold
                            if m1.distance < 0.75*m2.distance and m1.distance <= 150:
                                    gcount += 1
                    # only conclude a match if there are at least 20 good feature pairs
                    if gcount >= 20:
                            clusters[features[i][0]].append(
                                    features[j][0]
                            )
    return clusters
