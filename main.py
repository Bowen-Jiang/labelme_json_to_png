import os
import numpy as np
import cv2
import shutil

def Json2png(input_path,temp_path,mask_path):
    json_path = os.listdir(input_path)
#     print(json_path)
    for file_name in json_path:
        if file_name.endswith('.json'):
            file_name_path = os.path.join(input_path+"/"+ file_name)
            print("file_name_path:",file_name_path)
            file_name_noext = os.path.splitext(file_name)[0]
            print("file_name_noext:",file_name_noext)
            temp_dir = os.path.join(temp_path +"/"+file_name_noext)
            print("output_dir:",temp_dir)

            labelme_str = "python json_to_dataset.py "+str(file_name_path)+" -o "+str(temp_dir)
            print("labelme_str:",labelme_str)
            os.system(labelme_str)

            #pop-up slam input format
            raw_file = os.path.join(temp_dir + "/" + "img.png")
            img_file = os.path.join(temp_dir + "/" + "label.png")
            raw = cv2.imread(raw_file)
            raw = cv2.resize(raw,(640,360), interpolation=cv2.INTER_CUBIC)
            img = cv2.imread(img_file,cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img,(640,360), interpolation=cv2.INTER_CUBIC)
            #print(raw.shape)
            #print(img.shape)
#             cv2.imshow(file_name_noext+"_raw",raw)
#             cv2.imshow(file_name_noext,img)
#             cv2.waitKey(0)

            #二值化
            thres = 1
            img_binary = cv2.threshold(img, thres, 255, cv2.THRESH_BINARY)[1]
#             cv2.imshow("binary",img_binary)
#             cv2.waitKey(0)
            
            #save
            img_raw_file = os.path.join(mask_path+"/rgb_"+file_name_noext+".png")
            img_binary_file = os.path.join(mask_path+"/label_"+file_name_noext+".png")

            cv2.imwrite(img_raw_file,raw)
            cv2.imwrite(img_binary_file,img_binary)


if __name__ == "__main__":
    input_path = "data/label" 
    temp_path = "data/temp"
    mask_path = "data/output"
    
    #create folder
    os.makedirs(temp_path, exist_ok=True)
    os.makedirs(mask_path, exist_ok=True)
    
    Json2png(input_path,temp_path,mask_path)
