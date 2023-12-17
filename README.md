# Your personal posture assistant!

This app takes images from your laptop and check the developer posture using OpenAI Vision Model.

For the solution to work correctly:
     - Solution works when developers setup is using a laptop connected to a second monitor, keyboard and mouse. 
     - Laptop must be set aside, on the right or left side of the developers working station.
     - The laptop camera must capture the developer from the side

# Results

|Photo|GPT Vision Photo Description|GPT Posture Analysis|Result|
|:---:|:---:|:---:|:---:|
|img01.png|Person head is leaning down|Posture is ok|Correct|

# Dependencies
Install all the dependencies needed from the requirements.txt file: 
```bash
pip install requirements.txt
```

# Run
```bash
python.exe .\main.py
```