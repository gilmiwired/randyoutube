from apiclient.discovery import build
from flask import Flask
from flask import Flask, render_template #追加
import random, string

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

api_key = 'AIzaSyACME4_tgC7ydsp1JwO6qBtFuj4eKaodg4'

def get_videos_search(keyword):
    youtube = build('youtube', 'v3', developerKey=api_key)
    youtube_query = youtube.search().list(q=keyword, part='id,snippet', maxResults=5)
    youtube_res = youtube_query.execute()
    return youtube_res.get('items', [])

result = get_videos_search(randomname(random.randint(0,3)))
for item in result:
    if item['id']['kind'] == 'youtube#video':
        print("\n" + item['snippet']['title'] + "\n")
        a = 'https://www.youtube.com/watch?v=' + item['id']['videoId']



app = Flask(__name__)

@app.route('/')
def hello():
    name = a
    #return name
    return render_template('hello.html', title='flask test', name=name) #変更

## おまじない
if __name__ == "__main__":
    app.run(debug=True)