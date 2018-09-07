# Python Weather WebApp
Docker image
```
docker build -t spectrum/python-weather-webapp .
docker run --detach --name python-weather-webapp -p 4000:4000 spectrum/python-weather-webapp
docker stop <container_id>
docker rm <container_id>
```

Test application: [http://localhost:4000/](http://localhost:4000/)
