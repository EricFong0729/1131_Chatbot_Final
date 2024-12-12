import requests
import configparser

# 讀取 config.ini 檔案
config = configparser.ConfigParser()
config.read('config.ini')

# 獲取 API key
api_key = config['tmdb']['api_key']

# 取得電影名稱
query=""
url = "https://api.themoviedb.org/3/search/movie?query="++"&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNDAyOGQwMWE3YTgzYjZjZmIyZTQ1OGRkOWU2YjNmNCIsIm5iZiI6MTczMzg4NTc1MS4xMjQsInN1YiI6IjY3NThmZjM3MzU5ZGM1ZmM4ODNmMGRkYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8q7p7jgB2m46go5a0KBV1uc3sLeflCmsGWjfb26R1hA"
}

response = requests.get(url, headers=headers)

print(response.text)