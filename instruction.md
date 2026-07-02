There is an access log located at `/app/access.log` in the working directory. Analyze the traffic and summarize what you find. 

Your task is to calculate the total number of requests, the count of unique client IP addresses, and find the most popular request path. Save these findings into a JSON file at `/app/report.json`.

The JSON structure must match the following format exactly:
```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
