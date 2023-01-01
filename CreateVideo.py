import cv2
import os
path='Images/'
Images = []
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        Images.append(file_name)
        
print(len(Images))
count = len(Images)
frame=cv2.imread(Images[0])
height,width,channels=frame.shape
size=(width,height)
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'),
      5, size)
for i in range(0,count-1):
    frame=cv2.imread(Images[i])
    out.write(frame)
out.release()    
