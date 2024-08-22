import os
idl_file_dir = "./dataset/brainwash/brainwash_train.idl"
txt_files_dir = "./dataset/brainwash/val/labels"

if not os.path.exists(txt_files_dir):
    os.mkdir(txt_files_dir)
f1 = open(idl_file_dir, 'r+')
lines = f1.readlines()
#print(range(len(lines)))
for i in range(len(lines)):
    line = lines[i]
    line = line.replace(":", ";")
    #print(line)
    img_dir = line.split(";")[0]
    #print(img_dir)
    img_boxs = line.split(";")[1]
    img_dir = img_dir.replace('"', "")
    #print(img_dir)
    img_name = img_dir.split("/")[1]
    txt_name = img_name.split(".")[0]
    img_extension = img_name.split(".")[1]
    #print(txt_name)
    #print(img_extension)
    img_boxs = img_boxs.replace(",", "")
    #print(img_boxs)
    img_boxs = img_boxs.replace("(", "")
    img_boxs = img_boxs.split(")")
    #print(img_boxs)
    #print(type(img_boxs))
    if (img_extension == 'png'):
        for n in range(len(img_boxs) - 1):
                box = img_boxs[n]
                box = box.split(" ")
                # print(box)
                # print(box[4])
                if img_boxs:
                    with open(txt_files_dir + "/" + txt_name + ".txt", 'a') as f:
                        f.write(' '.join(['0', str((float(box[1]) + float(box[3])) / (2 * 640)),
                                          str((float(box[2]) + float(box[4])) / (2 * 480)),
                                          str((float(box[3]) - float(box[1])) / 640),
                                          str((float(box[4]) - float(box[2])) / 480)]) + '\n')
        if len(img_boxs)==1:
            with open(txt_files_dir + "/" + txt_name + ".txt", 'a') as f:
                f.write('')



