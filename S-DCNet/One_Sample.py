import os
import shutil
import numpy as np
from main_process import main_1
from IOtools import txt_write
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def openfile_gui():
    root = tk.Tk()
    root.filenames = filedialog.askopenfilename(title="Select File",
                                                filetypes=[
                                                    ("image", "*.jpg"),
                                                    ("image", "*.jpeg"),
                                                    ("image", "*.png"),
                                                ])
    if not root.filenames:
        openfile_gui()
    else:
        root.destroy()
        return root.filenames


if __name__ == '__main__':
    filenames = openfile_gui()
    print('File:', filenames)
    shutil.copyfile(filenames, './Test_Data/Sample_One/test/images/IMG_1.jpg')



    opt = dict()

    dataset_list = {0:  'Sample_One'}
    model_list = {0: 'model/SHA'}
    max_num_list = {0: 22}

    # step1: Create root path for dataset
    opt['num_workers'] = 0

    opt['IF_savemem_test'] = False
    opt['test_batch_size'] = 1

    # --Network settinng
    opt['psize'], opt['pstride'] = 64, 64

    # -- start testing
    opt['dataset'] = dataset_list[0]
    opt['trained_model_path'] = model_list[0]
    opt['root_dir'] = os.path.join(r'Test_Data', opt['dataset'])

    # -- set the max number and partition
    opt['max_num'] = max_num_list[0]
    partition_method = {0: 'one_linear', 1: 'two_linear'}
    opt['partition'] = partition_method[1]
    opt['step'] = 0.5

    print('==' * 36)
    main_1(opt)
    print(filenames)
    img_temp = mpimg.imread(filenames)
    plt.imshow(img_temp)
    plt.show()
