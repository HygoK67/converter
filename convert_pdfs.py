import time

import pypdfium2 # Needs to be at the top to avoid warnings
import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1" # For some reason, transformers decided to use .isin for a simple op, which is not supported on MPS

import argparse
from marker.convert import convert_single_pdf
from marker.logger import configure_logging
from marker.models import load_all_models

from marker.output import save_markdown

# configure_logging()


os.makedirs("./converted", exist_ok=True)
output_folder = "./converted"
batch_multiplier = 6
model_lst = load_all_models()
path_dir = "./src_files/src_pdfs"
for filename in os.listdir(path_dir):
    filename = os.path.join(path_dir,filename)
    print(filename)
    full_text, images, out_meta = convert_single_pdf(filename, model_lst, batch_multiplier=batch_multiplier)
    fname = os.path.basename(filename)
    subfolder_path = save_markdown(output_folder, fname, full_text, images, out_meta)
    print(f"Convert {filename} markdown to the {subfolder_path} folder")