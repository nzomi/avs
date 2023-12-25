import yaml
import os
import glob

class_B = {'BasketballDrive_1920x1080_50', 'BQTerrace_1920x1080_60', 
           'Cactus_1920x1080_50', 'Kimono1_1920x1080_24',
           'ParkScene_1920x1080_24',
           }
class_C = {'asketballDrill_832x480_50', 'QMall_832x480_60',
           'PartyScene_832x480_50', 'RaceHorses_832x480_30',
           }
class_D = {'BasketballPass_416x240_50', 'BlowingBubbles_416x240_50',
           'BQSquare_416x240_60', 'RaceHorses_416x240_30',
           }
class_E = {'FourPeople_1280x720_60', 'Johnny_1280x720_60',
           'KristenAndSara_1280x720_60',
           }

def process():
    HEVC_DATA = glob.glob('data/*.yml')
    HEVC_B, HEVC_C, HEVC_D, HEVC_E = {}, {}, {}, {}  
    rate = float(2048.0)   
    for file_name in HEVC_DATA:
        cur_class = file_name.split('\\')[-1].split('.')[0]
        with open(file_name, 'r') as f:
            cur_file = yaml.load(f, Loader=yaml.FullLoader)
        if cur_class in class_B:
            HEVC_B[cur_class] = {rate: {}}
            HEVC_B[cur_class][rate]['bpp'] = cur_file['all_frame_avg']['rate']
            HEVC_B[cur_class][rate]['psnr'] = cur_file['all_frame_avg']['distortion']
            for i in range(96):
                HEVC_B[cur_class][rate][i]={}
                HEVC_B[cur_class][rate][i]['bpp'] = cur_file['rate'][i]
                HEVC_B[cur_class][rate][i]['psnr'] = cur_file['distortion'][i]
                HEVC_B[cur_class][rate][i]['frame_type'] = cur_file['frames_type'][i].upper()
        if cur_class in class_C:
            HEVC_C[cur_class] = {rate: {}}
            HEVC_C[cur_class][rate]['bpp'] = cur_file['all_frame_avg']['rate']
            HEVC_C[cur_class][rate]['psnr'] = cur_file['all_frame_avg']['distortion']
            for i in range(96):
                HEVC_C[cur_class][rate][i]={}
                HEVC_C[cur_class][rate][i]['bpp'] = cur_file['rate'][i]
                HEVC_C[cur_class][rate][i]['psnr'] = cur_file['distortion'][i]
                HEVC_C[cur_class][rate][i]['frame_type'] = cur_file['frames_type'][i].upper()
        if cur_class in class_D:
            HEVC_D[cur_class] = {rate: {}}
            HEVC_D[cur_class][rate]['bpp'] = cur_file['all_frame_avg']['rate']
            HEVC_D[cur_class][rate]['psnr'] = cur_file['all_frame_avg']['distortion']
            for i in range(96):
                HEVC_D[cur_class][rate][i]={}
                HEVC_D[cur_class][rate][i]['bpp'] = cur_file['rate'][i]
                HEVC_D[cur_class][rate][i]['psnr'] = cur_file['distortion'][i]
                HEVC_D[cur_class][rate][i]['frame_type'] = cur_file['frames_type'][i].upper()
        if cur_class in class_E:
            HEVC_E[cur_class] = {rate: {}}
            HEVC_E[cur_class][rate]['bpp'] = cur_file['all_frame_avg']['rate']
            HEVC_E[cur_class][rate]['psnr'] = cur_file['all_frame_avg']['distortion']
            for i in range(96):
                HEVC_E[cur_class][rate][i]={}
                HEVC_E[cur_class][rate][i]['bpp'] = cur_file['rate'][i]
                HEVC_E[cur_class][rate][i]['psnr'] = cur_file['distortion'][i]
                HEVC_E[cur_class][rate][i]['frame_type'] = cur_file['frames_type'][i].upper()
    
    data = HEVC_B
    yaml_file_path = f'dst/HEVC_B_gop32.yaml'
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.safe_dump(data, yaml_file)
    
    data = HEVC_C
    yaml_file_path = f'dst/HEVC_C_gop32.yaml'
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.safe_dump(data, yaml_file)
    
    data = HEVC_D
    yaml_file_path = f'dst/HEVC_D_gop32.yaml'
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.safe_dump(data, yaml_file)
    
    data = HEVC_E
    yaml_file_path = f'dst/HEVC_E_gop32.yaml'
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.safe_dump(data, yaml_file)
                
process()