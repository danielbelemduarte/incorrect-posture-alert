import cv2
import os
from utils import read_prompt, play_alert, load_config_file, check_if_folder_exists, create_folder
import time
from openai import OpenAI
import json

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

    loaded_vision_prompt =  read_prompt("prompt_analyze_photo_vision.txt")

    payload = {
    "model": vision_model,
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": f"{loaded_vision_prompt}"
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

    return str(answer)

def analyze_posture_description(posture_analysis_description, completion_model, api_key):
    client = OpenAI()
    client.api_key = api_key

    system_message = read_prompt("prompt_analyze_posture_description_system_message.txt")
    user_message = read_prompt("prompt_analyze_posture_description_user_message.txt").replace("<<POSTURE_DESCRIPTION>>", posture_analysis_description)


    response = client.chat.completions.create(
    model=completion_model,
    response_format={ "type": "json_object"},
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

if __name__ == "__main__":

    project_setup_config()

    config_file = load_config_file()

    VISION_MODEL_NAME = config_file['vision_model_name']
    COMPLETION_MODEL_NAME = config_file['completion_model_name']
    MAX_TOKENS = config_file['max_tokens']
    TIMER_CHECKER_SECONDS = config_file['timer_check_seconds']

    # OPENAI API KEY MUST BE ADDED TO THE SYSTEM ENVIRONMENT VARIABLES WITH THE NAME ON THE CONFIG FILE 
    OPENAI_API_KEY_ENVNAME = config_file['envname_openai_api_key']
    OPENAI_API_KEY = os.getenv(OPENAI_API_KEY_ENVNAME)

    while True:
        img_filename = save_frame_camera_key(0, 'data/temp', 'camera_capture')
        img_filename = img_filename.replace("/", "\\")

        posture_analysis_result = call_vision(image_path=img_filename, api_key=OPENAI_API_KEY, vision_model=VISION_MODEL_NAME, max_tokens=MAX_TOKENS)

        print("Posture analysis from VISION:")
        print(posture_analysis_result)

        posture_result_payload = analyze_posture_description(posture_analysis_result, COMPLETION_MODEL_NAME, OPENAI_API_KEY)

        print("Posture result from GPT:")
        print(posture_result_payload)

        parsed_json = json.loads(posture_result_payload)
        posture = parsed_json["response"]

        if "incorrect" in str(posture).lower():
            print("You are in an INCORRECT working posiiton!")
            play_alert()
        elif "correct" in str(posture).lower():
            print("You are in a CORRECT working posiiton!")
        else:
            print("Model could not confirm the position, check if images are capturing your body and posture for correct analysis!")
        # Wait for 5 minutes
        time.sleep(TIMER_CHECKER_SECONDS)
