#Just a little mandelbrot demo, 2026/07/23
#no ai used
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt

def mandelbrot():
    #print("Hallo")

    w, h = 1024, 512  #determines the resolution of the output image

    maxiter = 100    #number of max iterations, higher values lead to more precise and detailed results
    threshold = 2    #to determine if the series does not converge, everything above to reaches infinity

    data = np.zeros((h, w, 3), dtype=np.uint8)
    ##data[0:256, 0:256] = [255, 0, 0]  # red patch in upper left


    for x in range (w):
        for y in range (h):
            c = complex(x/(h/2)-2, y/(h/2)-1)
            z = complex(0, 0)
            #print(c)
            for it in range(maxiter):
                z = z*z + c
                if z.__abs__() > threshold:
                    data[y,x] = [it * 255/maxiter,0,0]
                    #the most iterations which only exceed the threshold in the end lead to the brightest colors, large numbers darker that don't converge, exceed the bound quicker and are painted darker.
                    #print(it)
                    break

    img = Image.fromarray(data, 'RGB')
    img.save('mandelbrot.png')
    img.show()

    #plt.imshow(img)

mandelbrot()
