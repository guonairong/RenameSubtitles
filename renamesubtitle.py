# coding:utf-8
import os,sys
import re

mediaExtList=[".mkv",".avi",".rmvb"]
subtitleExtList=[".srt",".ass"] 

gMediaFileList=[]
gSubFileList=[] 

mediaNamePattern = re.compile(r"(.*?)([sS]\d+[eE]\d+)(.*?)")
def renameMedia():
    for mediaFile in gMediaFileList:
        #print mediaFile
        baseFile=os.path.splitext(mediaFile)[0]
        #print baseFile
        filename = os.path.basename(mediaFile)
        matched = mediaNamePattern.match(filename)
        if matched:           
            episode = matched.group(2)
            subFile = getFirstMathedEpisode(episode)
            if subFile:
                #print "sbufile="+subFile
                subExt=os.path.splitext(subFile)[1]
                if subFile.find(baseFile)!=0:                
                    print "rename %s  to %s"%(subFile, baseFile+subExt)
                    os.rename(subFile,baseFile+subExt)
                    
           
def getFirstMathedEpisode(episode):
    for subFile in gSubFileList:
        if subFile.find(episode)>=0:
            return subFile
    return None        
           
    
def walkIn(rootPath):
    filelist = os.listdir(rootPath)
    for line in filelist:
        #print line
        subfilepath = os.path.join(rootPath,line)
        if os.path.isfile(subfilepath):
            #print os.path.splitext(line)
            if os.path.splitext(line)[1] in mediaExtList:
                gMediaFileList.append(subfilepath)
            elif os.path.splitext(line)[1] in subtitleExtList:        
                gSubFileList.append(subfilepath)


if __name__ == "__main__":
    rootPath = "." 
    if len(sys.argv)==2:
        rootPath = sys.argv[1]    
    walkIn(rootPath)
    renameMedia()
                 

