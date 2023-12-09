import cv2
import os
from utils import read_prompt, play_alert, load_config_file, check_if_folder_exists, create_folder
import time

# used to create folders and project structure if do not exist
def project_setup_config():
    # temp folder must exist
    folder_name = "data/temp"
    if (not check_if_folder_exists(folder_name)):
        create_folder(folder_name)

    # use this function to initialize anything needed

def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    # TODO generate new image each time 
    sequence = 0
    ret, frame = cap.read()
    cv2.imshow(window_name, frame)
    image_filename = '{}_{}.{}'.format(base_path, sequence, ext)
    cv2.imwrite(image_filename, frame)

    cv2.destroyWindow(window_name)
    return image_filename

def call_vision(image_path, api_key, vision_model, max_tokens):
    import base64
    import requests

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    loaded_prompt =  read_prompt("prompt.txt")

    payload = {
    "model": vision_model,
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": f"{loaded_prompt}"
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": max_tokens
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    answer = response.json()['choices'][0]['message']['content']

    #print(response.json())
    print("Answer: " + str(answer))
    return str(answer)


if __name__ == "__main__":

    project_setup_config()

    config_file = load_config_file()
    MODEL_NAME = config_file['model_name']
    MAX_TOKENS = config_file['max_tokens']

    # OPENAI API KEY MUST BE ADDED TO THE SYSTEM ENVIRONMENT VARIABLES WITH THE NAME ON THE CONFIG FILE 
    OPENAI_API_KEY_ENVNAME = config_file['envname_openai_api_key']
    OPENAI_API_KEY = os.getenv(OPENAI_API_KEY_ENVNAME)

    while True:
        img_filename = save_frame_camera_key(0, 'data/temp', 'camera_capture')
        img_filename = img_filename.replace("/", "\\")

        result = call_vision(image_path=img_filename, api_key=OPENAI_API_KEY, vision_model=MODEL_NAME, max_tokens=MAX_TOKENS)

        print("Posture analysis:")
        print(result)

        if "curved" in result.lower():
            print("You are in an INCORRECT working posiiton!")

            play_alert()

        elif "straight" in result.lower():
            print("You are in a CORRECT working posiiton!")
        else:
            print("Model could not identify the position, check if images are capturing your body and posture for correct analysis!")
        # Wait for 5 minutes
        time.sleep(300)  # 300 seconds = 5 minutes


