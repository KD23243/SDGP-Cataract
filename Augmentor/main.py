import os
import shutil
import Augmentor
import cv2


def resize_img(im):
    resized_img = cv2.resize(im, (51, 51))
    return resized_img


def create_samples(dir):
    p = Augmentor.Pipeline("cataract")

    p.rotate(probability=1, max_left_rotation=5, max_right_rotation=5)
    p.flip_left_right(probability=0.5)
    p.zoom_random(probability=0.5, percentage_area=0.8)
    p.flip_top_bottom(probability=0.5)
    p.sample(100)


if __name__ == '__main__':
    dir_list = ['neg', 'info']
    dest = "input_path"
    # lets create a sample of 1000 negative and 1000 positive Images
    for img_dir in dir_list:
        print("************************Processing {0} Directory*****************************".format(img_dir))
        create_samples(img_dir)
        # Now lets move files created to input_path folder
        source = img_dir + "/output/"
        dest = dest + "_{0}".format(img_dir)
        files = os.listdir(source)
        for f in files:
            shutil.move(source + f, dest)
        dest = "input_path"
        print("********************************************************************************")

    # # This loop will resize all imaes to 128*128*3
    # for img_dir in dir_list:
    #     # create_samples(img_dir)
    print("************************Starting the resize process*****************************".format(img_dir))
    for root, dirs, files in os.walk(dest):
        for file in files:
            filefullpath = os.path.join(root, file)
            if filefullpath.endswith('.jpg') or filefullpath.endswith('.JPG'):
                im_read = cv2.imread(filefullpath)
                resized_img = resize_img(im_read)
                print("[INFO] Writing converted {0} file".format(filefullpath))
                cv2.imwrite(filefullpath, resized_img)
