# API-Flask-MySQL

REST API 

## Tutorial

1️⃣ - Make sure you have installed Python and Docker 👇

* Download [Python](https://www.python.org/downloads/)
* Donwload [Docker](https://docs.docker.com/desktop/windows/install/)

2️⃣ - Download files [here](https://github.com/Ewerton12F/API-Flask-MySQL/archive/refs/heads/master.zip) or clone the project 👇

```shell
git clone git@github.com:Ewerton12F/API-Flask-MySQL.git
```

3️⃣ - Once inside the main directory you can create a virtual enviroment and activate it 👇

```shell
virtualenv venv && source venv/bin/activate
```

4️⃣ - Build the Docker Image 👇

```shell
docker build -tag python-docker .
```

5️⃣ - Start the Docker Container 👇

```shell
docker run -d -p 5000:5000 python-docker
```

6️⃣ Go to 👉 http://localhost:5000/

---