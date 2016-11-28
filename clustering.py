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
                    needed = max(int(0.1*min(len(pdes), len(sdes))), 10)
                    gcount = 0

                    loweMatches = matcher.knnMatch(pdes, sdes, k=2)
                    for m1, m2 in loweMatches:
                            if m1.distance < 0.75*m2.distance and m1.distance <= 150:
                                    gcount += 1
                    if gcount >= 20:
                            clusters[features[i][0]].append(
                                    features[j][0]
                            )
    return clusters

def getCluster(fname, clusters, explored):
        cluster = clusters[fname]
        explored[fname] = True
        for related in clusters[fname]:
                if not explored[related]:
                        cluster += getCluster(related, clusters, explored)
        cluster += [fname]
        return cluster

def Cluster(clusters):
        c = []
        for filename in clusters:
                explored = {k: False for k in clusters}
                c.append(set(getCluster(filename, clusters, explored)))
        return c 
