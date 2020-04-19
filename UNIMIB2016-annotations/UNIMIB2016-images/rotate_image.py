from PIL import Image, ExifTags
import matplotlib.pyplot as plt
import numpy as np
import os
from tqdm import tqdm

# filepath = r"D:\Users\Enzo\Downloads\UNIMIB2016-images (1)\original\20151127_115424.jpg"
# filepath = r"D:\\Users\\Enzo\Downloads\\UNIMIB2016-images\\20151204_130528.jpg"

dataset_folder = r"D:\\Users\\Enzo\\Downloads\\UNIMIB2016-images\\original"
save_folder = r"D:\Users\Enzo\Downloads\UNIMIB2016-images\rotated_images"

filenames = os.listdir(dataset_folder)
# print (filenames)
counter = 0
for filepath in tqdm(filenames):
    # print(filepath)
    
    try:
        image=Image.open(os.path.join(dataset_folder, filepath))
        # print(ExifTags.TAGS.keys())
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                # print("180")
                break

        exif=dict(image._getexif().items())
        # print(exif)
        
        print("{}: {}".format(exif[orientation], filepath))
        
        if exif[orientation] == 3:
            image=image.rotate(180, expand=True)
            image=image.rotate(180, expand=True)
            # print("180")
        elif exif[orientation] == 6:
            image=image.rotate(360, expand=True)
            # print("90 CCW")
        elif exif[orientation] == 8:
            image=image.rotate(0, expand=True)
            # print("90 CW")

        # image.show(img)
        # plt.imshow(image)
        # plt.show()
        
        scale_percent = 10
        width, height = image.size  

        width1 = width//scale_percent
        height1 = height//scale_percent

        image = image.resize((width1, height1))
        
        image.save(os.path.join(save_folder, filepath))
        image.close()
    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass
    counter = counter + 1