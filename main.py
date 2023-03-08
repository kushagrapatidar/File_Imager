from reader import readstr
from convert import converttopxl,setpxlval
from converttoascii import toascii
from imagedimensions import getdimensions
from manipulateimg import saveimg

#Name of the file with extension
fname=input('Enter the name of the file: ')

#Read the file
string=readstr(fname)
#print(type(codestr))

#Convert to ASCII
strascii=toascii(string)
# print(strascii)
# print(len(strascii))

#Calculate the pixel values
pxls=converttopxl(strascii)
# [print(pxl) for pxl in pxls]
#print(len(pxls))

#Get the Dimensions of the image
pxls,width,height=getdimensions(pxls)
# print(pxls,width,height)

#Set the pixel values in Image
img=setpxlval(width,height,pxls)
# print(img)

#Save the image
imgname,imglocation=saveimg(fname,img)
print("Your image is saved successfully at "+imglocation+" as "+imgname)