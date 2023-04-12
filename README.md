# memos-add-tag

```
docker build -t memos-add-tag .
docker run -d --restart=always -p 5000:5000 -e api_key=<your-api-key> -e open-api=<your-memos-open-api> memos-add-tag
```
