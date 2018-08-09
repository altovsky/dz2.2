# -*- coding: utf-8 -*-


import subprocess
import os

source = 'Source'
result = 'Result'
convert = 'convert'
convert_cmd = '-resize 200'

current_dir = os.path.dirname(os.path.abspath(__file__))

source_path = os.path.join(current_dir, source)
result_path = os.path.join(current_dir, result)
convert_path = os.path.join(current_dir, convert)

if not os.path.isdir(result):
    os.mkdir(result_path)

image_list = os.listdir(source_path)

for image_name in image_list:
    image_source_path = os.path.join(source_path, image_name)
    image_result_path = os.path.join(result_path, image_name)

    run_path = f'{convert_path} {image_source_path} {convert_cmd} {image_result_path}'

    proc = subprocess.Popen(run_path, shell=True, stdout=subprocess.PIPE)
    out = proc.communicate()
