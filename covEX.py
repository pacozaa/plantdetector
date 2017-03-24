import cv2
import numpy as np
import os


def calEXG(red,green,blue):
    result = 2*green-red-blue
    return result

def calEXR(red,green,blue):
    result = 1.5*red-green-blue
    return result

def savePlants(savename,plantimg,exgimg,exgimgblurred,original,notblurred,blurred,otsu,extension):
    cv2.imwrite(savename+'/'+original+extension,plantimg)
    cv2.imwrite(savename+'/'+notblurred+extension,exgimg)
    cv2.imwrite(savename+'/'+blurred+extension,exgimgblurred)

    # ret2,th2 = cv2.threshold(exgimgblurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # cv2.imwrite(savename+'/'+otsu+extension,th2)


def convertGreenSerious(rawimg):
    blue = rawimg[:,:,0]
    green = rawimg[:,:,1]
    red = rawimg[:,:,2]
    exg = 1.5*green-red-blue
    processedimg = np.where(exg > 50, exg, 0)

    return processedimg

def convertGreenPlant(rawimg):
    blue = rawimg[:,:,0]
    green = rawimg[:,:,1]
    red = rawimg[:,:,2]
    exg = 1.5*green-red-blue
    processedimg = np.where(exg > 50, exg, 0)

    return processedimg

def convertRed(rawimg):
    blue = rawimg[:,:,0]
    green = rawimg[:,:,1]
    red = rawimg[:,:,2]
    exg = 1.5*red-green-blue
    processedimg = np.where(exg > 50, exg, 0)

    return processedimg



def convertTofile(filepath,filename,extension,savepath):
    directory = filepath+filename+extension
    plantimg = cv2.imread(directory)

    exgimg = convertGreen(plantimg)
    exgimgblurred = cv2.GaussianBlur(exgimg,(5,5),0)

    if not os.path.exists(savepath+filename):
        os.makedirs(savepath+filename)

    savePlants(savepath+filename,plantimg,exgimg,exgimgblurred,'original','notblurred','blurred','otsu','.png')
