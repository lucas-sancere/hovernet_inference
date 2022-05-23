#!/bin/bash -l
#SBATCH --partition=zmmk-exclusive

#SBATCH --mem=128G
#SBATCH --gres=gpu:2
#SBATCH --cpus-per-task=32
#SBATCH --time=7-12:00:00

#SBATCH --job-name=tr_1
#SBATCH --output=/projects/ag-bozek/lucas/Hover_Net_Complete/tensorflow-inference/hovernet_inference/output_1.txt
#SBATCH --mail-type=BEGIN,END,FAIL

### begin of executable commands
conda activate hovernet_inference
python run.py --gpu='0' --mode='tile' --model='pannuke.npz' --input_dir='../data_hovernet_inference/wsi_mode/Inputs' --output_dir='../data_hovernet_inference/wsi_mode/Outputs'
