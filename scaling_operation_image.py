import cv2

def main():
    
    path = "C:\\Users\\Vedhanarayanan\\Documents\\Python\\data-mites\\computer vision\\image\\"
    
    imgpath1 =  path + "lena.tiff"
    img1 = cv2.imread(imgpath1, 1)

    
    output = cv2.resize( img1, None, fx=0.5, fy=1.5, interpolation=cv2.INTER_AREA )
   
    
    cv2.imshow('Output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()
