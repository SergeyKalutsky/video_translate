import os
import shutil
from tqdm import tqdm
from gtts import gTTS

shutil.rmtree('translated')
os.mkdir('translated')
with open('translate.txt', 'r', encoding='utf-8') as f:
    data = [i.replace('\n', '') for i in f.readlines()]
    
for i, text in tqdm(enumerate(data)):
    audio = gTTS(text=text, lang="en", slow=False)
    audio.save(f"translated/{i}.mp3")
