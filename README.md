# Your personal posture assistant!

This app takes images from your laptop and checks your posture while working at a desk.
It leverages OpenAI Vision Model to interpret the images and analyze the body posture.

For the solution to work correctly:
* The image must be captured from the left or right side of the working stationg. You can you a webcam or your laptop if it is place on the side
* The must be good light on the room for the image to have good quality

The high-level architecture is as follows:

![picture alt](https://i.ibb.co/4tnvn9Q/hl-architecture.png "High-level architecture")

# Results

|Photo|GPT Vision Photo Description|GPT Posture Analysis|Result|
|:---:|:---:|:---:|:---:|
|![picture alt](https://i.ibb.co/5Kf7h5w/img-correct-posture-blurr.jpg "img_correct_posture.png")|The person depicted in the photo is sitting with their torso turned slightly to the side. Observations based on the posture are as follows: <ul><li>The neck position is fairly straight, not leaning down or appearing curved.</li><li>The back position is not entirely visible due to the angle, but it does not appear to be significantly curved.</li><li>The shoulders position seems to be in a natural state, not particularly rounded to the front or drawn downwards.</li><li>The chin position is not closed to the chest but held at a normal distance, giving the impression of an aligned posture.</li><li>The eyes are looking forward rather than downward, in line with a forward facing orientation.</li><li>The head position is straight, looking forward, parallel to the line of sight, suggesting attentiveness or engagement with something beyond the table.</li></ul> |{"response": "CORRECT"} | Correct |
|![picture alt](https://i.ibb.co/CwrZ8db/img-incorrect-posture-blurr.jpg "img_incorrect_posture.png")|The person in the photo appears to have their neck slightly curved and leaning down as they focus on something on the table. Their back is not visible in this image, but the way the shoulders are positioned suggests a slight forward curvature in the upper spine. The shoulders appear to be slightly rounded to the front, indicating a hunched posture. The chin is closer to the chest than it would be in an upright posture, reinforcing the overall forward-leaning position. The eyes are looking down towards the table, which seems to be aligned with the work-related activity the person is engaged in. Consequently, the head is also leaning down rather than looking forward, which could suggest engagement in reading, writing, or possibly using a device on the table (though none is visible in the image). Maintaining such a posture for extended periods could potentially lead to discomfort or strain, and it might be beneficial for the person to adjust positioning for better ergonomic alignment. |{"response": "INCORRECT"} | Incorrect |

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