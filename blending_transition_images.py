import cv2
import numpy as np
import time
#import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\Vedhanarayanan\\Documents\\Python\\data-mites\\computer vision\\image\\"
    
    imgpath1 =  path + "lena.tiff"
    imgpath2 =  path + "maxy.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
#    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    for i in np.linspace(0, 1, 100):
        alpha = i
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        cv2.imshow('Transition', output)
        time.sleep(0.02)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()