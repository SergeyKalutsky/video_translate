import requests
from tqdm import tqdm
from time import sleep
from text import parse_subtitles
from credentials import IAM_TOKEN, folder_id


def parse_response(response):
    sentences = []
    data = response.json()['translations']
    for sent in data:
        sentences.append(sent['text'])
    return sentences


texts, _ = parse_subtitles('text.txt')
url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {0}".format(IAM_TOKEN)
}

body = {
    "texts": [],
    "folderId": folder_id,
    'sourceLanguageCode': 'vi',
    "targetLanguageCode": 'en'
}

sentences = []
for i in tqdm(range((len(texts)//10)+1)):
    body['texts'] = texts[i*10:(i*10)+10]
    response = requests.post(url, json=body, headers=headers)
    sentences += parse_response(response)
    sleep(0.2)

with open('translate.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sentences))
