## You can build the Docker image using the following command:

```code
docker build -t flask-redis-app .
``` 

And then run the container with:

```code
docker run -p 5000:5000 flask-redis-app
```

This will map port 5000 from the container to port 5000 on your local machine, allowing you to access the Flask app at http://localhost:5000.