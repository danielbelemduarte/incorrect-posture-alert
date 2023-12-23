# Your personal posture assistant!

This app takes images from your laptop and checks your posture while working at a desk.
It leverages OpenAI Vision Model to interpret the images and analyze the body posture.

For the solution to work correctly:
* The image must be captured from the left or right side of the working stationg. You can you a webcam or your laptop if it is place on the side
* The must be good light on the room for the image to have good quality

The high-level architecture is as follows:

![picture alt](https://i.ibb.co/6Nr9Rdz/hl-architecture.png "High-level architecture")

# Results

|Photo|GPT Vision Photo Description|GPT Posture Analysis|Result|
|:---:|:---:|:---:|:---:|
|img01.png|Person head is leaning down|Posture is ok|Correct|

# Dependencies / Installation
Install all the dependencies needed from the requirements.txt file: 
```bash
pip install requirements.txt
```

You will need an OpenAI API Key to use the model. Get it from https://platform.openai.com/api-keys.
You must setup the OpenAI API Key as part of the Windows environment variables with the key: OPENAI_API_KEY and value being your generated API Key

# Run
```bash
python.exe .\main.py
```