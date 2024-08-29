export $(grep -v '^#' .env.google | xargs)

curl "https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key=$API_KEY&part=snippet,contentDetails,statistics,status"