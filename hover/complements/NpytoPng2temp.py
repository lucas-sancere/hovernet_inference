import os 
from os.path import join, getsize
import numpy as np
from PIL import Image as im


Outputdir = '/projects/ag-bozek/lucas/Hover_Net_Complete/tensorflow-inference/data_hovernet_inference/tile_mode/Outputs_sample_003_all_tiles/'

for root, dirs, files in os.walk(Outputdir):
    if files != []:
        npyarraypath = root + '/' + 'instances.npy'
        print('file converted:', npyarraypath)
        npyarray = np.load(npyarraypath)
        npyarray = npyarray.astype(np.uint8)
        data = im.fromarray(npyarray)
        data.save(npyarraypath.replace('.npy','.png'))
        
