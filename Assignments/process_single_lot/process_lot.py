# -*- coding: utf-8 -*-
"""
Team members:
1.Krishna Saka
2.Lavanya Mengaraboina
3.Keerthi Reddy Gangidi
"""
#importing required files
import numpy as np
import cv2 as cv
from scipy.spatial import distance
from matplotlib import pyplot as plt
from json import dumps,loads
import pprint as pp
from sys import argv, exit

#function for opening definition file in which we have the coordinates of each images
def load_spaces(definition_file):
    f = open(definition_file,'r')
    spaces = loads(f.read())

    return spaces
#functionfor extracting the coordinates values and storing them in a list
def extract_points(space):
    points = []
    for i in range(4):
        x = int(space['contour']['point'][i]['x'])
        y = int(space['contour']['point'][i]['y'])
        points.append((x,y))
        
    return points
#function for drawing the parking lot spaces on the image
def draw_parking_space(points,img):
    colors = [(0,0,255),(0,255,0),(255,0,0),(255,255,0)]
    for i in range(4):
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[(i+1)%4][0]
        y2 = points[(i+1)%4][1]
        cv.line(img, (x1,y1),(x2,y2),colors[i], 2)
        #plt.imsave(filenames[0],img)
#function for making a parallelogram and calculating distances between points
def make_parallelogram(p,type=0):
    """
    Types: 0 = smallest area , 1 = largest area , 2 = avg area
    """
    for i in range(4):
        a = p[i]
        b = p[(i+1) % 4]
        dst = distance.euclidean(a,b)
        print(dst)
    print()
#main starts from here
if __name__=='__main__':

    
    #initialising definition_file with json file and image_file with jpg file
    definition_file = 'C:\\Users\\keerthi\\.spyder-py3\\project1.json'
    image_file = 'C:\\Users\\keerthi\\.spyder-py3\\2012-12-07_17_12_25.jpg'

    spaces = load_spaces(definition_file)
    s=0
    img = cv.imread(image_file)
    for space in spaces:
        
        points = extract_points(space)
        cody = points[0][1]
       
        codX = points[1][0]
      
        codY = points[2][1]
        codx = points[3][0]
#croping the images with above coordinates and saving them in spaces folder
        crop_img = img[cody:codY,codx:codX]
        cv.imwrite("spaces/"+ str(s) +".png", crop_img)
        s=s+1
        
        make_parallelogram(points)
        draw_parking_space(points,img)
#plotting a histogram and saving them in histograms folder
        hist = cv.calcHist([crop_img], [0, 1], None, [180, 256], [0, 180, 0, 256])
        np.savetxt('histograms/'+str(s)+".csv", hist, delimiter=',')
        s=s+1
     
    

    
