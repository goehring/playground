#Just a little mandelbrot demo, 2026/07/23
#no ai used
import numpy as np
from PIL import Image

def mandelbrot():
    #print("Hallo")

#    w, h = 3840, 2048
    w, h = 1024, 512

    maxiter = 100

    data = np.zeros((h, w, 3), dtype=np.uint8)
    ##data[0:256, 0:256] = [255, 0, 0]  # red patch in upper left


    for x in range (w):
        for y in range (h):
            c = complex(x/(h/2)-2, y/(h/2)-1)
            z = complex(0, 0)
            #print(c)
            for it in range(maxiter):
                z = z*z + c
                if z.__abs__() > 100:
                    data[y,x] = [it * 255/maxiter,0,0]
                    #the most iterations lead to the brightest colors, large numbers darker that don't converge, exceed the bound quicker and are painted darker.
                    #print(it)
                    break

    img = Image.fromarray(data, 'RGB')
    #img.save('foo.png')
    img.show()

    pass



mandelbrot()
