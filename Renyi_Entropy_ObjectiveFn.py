import numpy as np
from PIL import Image
from math import log
import sys.float_info.epsilon as eps

def Renyi(Thresholds,image):
    Thresholds.append(255)
    Thresholds.append(-1)
    Thresholds.sort()
    
    img = Image.open(image).convert("L")
    img=np.asarray(img)

    hist = [0] * 256               
    for i in range(len(img)):
        for j in range(len(img[0])):
            hist[int(img[i][j])] += 1

    Total_Pixels = len(img)*len(img[0])

    for i in range(len(hist)):                                              # Probabilities
        hist[i] = hist[i] / Total_Pixels
    
    alpha=0.5                                                               # Alpha parameter
    H_alpha=[]

    for i in range(len(Thresholds)-1):
        cumulative_class_sum=(sum(hist[Thresholds[i]+1:Thresholds[i + 1]+1]))+eps
        H=0
        for j in range(Thresholds[i+1]+1):
            H+=(hist[j]/cumulative_class_sum)**alpha
        H_alpha.append((1/(1-alpha))*log(H+eps))
    
    return(sum(H_alpha))
