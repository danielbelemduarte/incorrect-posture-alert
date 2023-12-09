import os
from playsound import playsound
import yaml

def read_prompt(file_path: str): 
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
def play_alert():
    audio_path = "data\\alert-109578.mp3" 
    playsound(audio_path)

def load_config_file():
    # read params file
    with open('config.yml', 'r') as f:
        try:
            config_dic = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)

    return config_dic

def check_if_folder_exists(folder_path):
    if os.path.exists(folder_path):
        print(f"The folder '{folder_path}' exists.")
        return True
    else:
        print(f"The folder '{folder_path}' does not exist.")
        return False

def create_folder(folder_path):
    try:
        os.makedirs(folder_path)
        print(f"The folder '{folder_path}' has been created.")
    except OSError as e:
        print(f"Failed to create the folder '{folder_path}': {e}")