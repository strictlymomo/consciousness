import os

def save_transcript(video_id, data, type='json'):
    directory = f"./data/{type}/"
    filename = f"{video_id}.{type}"
    filepath = os.path.join(directory, filename)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(data)