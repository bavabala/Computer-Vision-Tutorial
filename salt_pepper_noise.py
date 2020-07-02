import cv2
import matplotlib.pyplot as plt
def main():
    
    path = "C:\\Users\\Vedhanarayanan\\Documents\\Python\\data-mites\\computer vision\\image\\"
    
    imgpath =  path + "maxy.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title('Image with Salt and Pepper Noise')
    plt.show()

if __name__ == "__main__":
    main()
