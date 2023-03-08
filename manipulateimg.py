def createimg(width,height):
    img = []
    for _ in range(height):
        row = []
        for _2 in range(width):
            row.append([255, 255, 255])
        img.append(row)
    return img

def definergb(width,height,img,pxls):
    i=0
    for _ in range(height):
        for _2 in range(width):
            img[_][_2]=pxls[i]
            i+=1
    return img

def saveimg(fname,img):
    from imageio import imsave
    from numpy import array as arr,uint8
    imglocation=input('Enter save location for image: ')
    imgname=fname.split('.')[0]
    imgname+=".jpeg"
    img=arr(img,dtype=uint8)
    imsave(imglocation+"\\"+imgname,img)
    return imgname,imglocation
