import os 
from os.path import join, getsize
import numpy as np
from PIL import Image as im


Outputdir = '/projects/ag-bozek/lucas/Data_General/Predictions/IHC_HE_ScieboData1/HE/Inputs_sample_008_overlappingVer_tiles_hovernet_inference/Outputs/'

for root, dirs, files in os.walk(Outputdir):
    if files != []:
        npyarraypath = root + '/' + 'instances.npy'
        print('file converted:', npyarraypath)
        npyarray = np.load(npyarraypath)
        npyarray = npyarray.astype(np.uint8)
        data = im.fromarray(npyarray)
        data.save(npyarraypath.replace('.npy','.png'))
        
