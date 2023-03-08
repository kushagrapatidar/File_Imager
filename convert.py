def converttopxl(strascii):
    pxls=list()
    for i in range(len(strascii)):
        rgb=[strascii[i]//3]*3
        rgb[1]+=strascii[i]%3
        pxls.append(rgb)
    return pxls

def setpxlval(width,height,pxls):
    from manipulateimg import createimg,definergb
    img=createimg(width,height)
    img=definergb(width,height,img,pxls)
    return img