# Secure Video Streaming over SSL with Python
This project demonstrates live video streaming over a secure SSL connection between a server and a client using Python. The server captures video frames from a webcam and sends them to the client over an encrypted connection. The client receives and displays the video feed.

## Requirements
1. Python 3.x
2. SSL certificates (server_cert.pem and server_key.pem for the server)
    To generate the SSL certificate (server_cert.pem) and private key (server_key.pem), run this command:
    ```bash
    openssl req -x509 -newkey rsa:4096 -keyout ssl/server_key.pem -out ssl/server_cert.pem -days 365
    ```

You can generate them using OpenSSL with the following command:

### Recommended: Virtual Environment Setup

It is recommended to use a virtual environment to isolate dependencies. Follow these steps to set up the environment:

1. **Install Python 3.10+** (if not already installed). You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a virtual environment**:
In your project directory, create a virtual environment using Python 3.10:
```bash
python3.10 -m venv venv
```

3. **Activate the virtual environment**:
    
    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    venv\Scripts\activate
```


Install required python packages by running
```
pip install -r requirements.txt
```

## Run the python files
Update the ip address in both files, and then run them
```
python server.py
```
```
python client.py
```
