import yaml
import os
import glob

class_B = frozenset({'BasketballDrive_1920x1080_50', 'BQTerrace_1920x1080_60', 
                    'Cactus_1920x1080_50', 'Kimono1_1920x1080_24',
                    'ParkScene_1920x1080_24'})
class_C = frozenset({'BasketballDrill_832x480_50', 'QMall_832x480_60',
                    'PartyScene_832x480_50', 'RaceHorses_832x480_30'})
class_D = frozenset({'BasketballPass_416x240_50', 'BlowingBubbles_416x240_50',
                    'BQSquare_416x240_60', 'RaceHorses_416x240_30'})
class_E = frozenset({'FourPeople_1280x720_60', 'Johnny_1280x720_60',
                    'KristenAndSara_1280x720_60'})

def process_class(class_name, rate):
    result = {}
    for cur_class in class_name:
        result[cur_class] = {rate: {}}
        with open(f'data/{cur_class}.yml', 'r') as f:
            cur_file = yaml.load(f, Loader=yaml.FullLoader)
        result[cur_class][rate]['bpp'] = cur_file['all_frame_avg']['rate']
        result[cur_class][rate]['psnr'] = cur_file['all_frame_avg']['distortion']
        for i in range(96):
            result[cur_class][rate][i] = {}
            result[cur_class][rate][i]['bpp'] = cur_file['rate'][i]
            result[cur_class][rate][i]['psnr'] = cur_file['distortion'][i]
            result[cur_class][rate][i]['frame_type'] = cur_file['frames_type'][i].upper()
    return result

def write_yaml_file(data, yaml_file_path):
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.safe_dump(data, yaml_file)

def process():
    rate = float(2048.0)
    
    HEVC_B = process_class(class_B, rate)
    HEVC_C = process_class(class_C, rate)
    HEVC_D = process_class(class_D, rate)
    HEVC_E = process_class(class_E, rate)

    write_yaml_file(HEVC_B, 'dst/HEVC_B_gop32_.yaml')
    write_yaml_file(HEVC_C, 'dst/HEVC_C_gop32_.yaml')
    write_yaml_file(HEVC_D, 'dst/HEVC_D_gop32_.yaml')
    write_yaml_file(HEVC_E, 'dst/HEVC_E_gop32_.yaml')

process()
