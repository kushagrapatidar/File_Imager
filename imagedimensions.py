def smoothpxls(pxls):
    num_extrapxls=144-(len(pxls)%144)
    extrapxls=[[255,255,255]]*num_extrapxls
    pxls=pxls+extrapxls
    return pxls
    
def getdimensions(pxls):
    num_pxls = len(pxls)
    if num_pxls%144!=0:
        pxls=smoothpxls(pxls)
        num_pxls = len(pxls)
    width,height=16*(num_pxls//144),9*(num_pxls//144)
    return pxls,width,height