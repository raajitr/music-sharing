## Music Streamer/Sharer/Management Mock Website

### Prequisites
- Python 3.7+

- For Python to work on Windows
    - [Download Windows executable](https://www.python.org/ftp/python/3.7.8/python-3.7.8-amd64.exe)
    - Open command prompt (Windows Key + R then type "cmd" and hit enter)
    - Type `python --version` and hit Enter. If you see the below message:
    ```
    'python' is not recognized as an internal or external command,
    operable program or batch file.
    ```
    then set [PYTHONPATH](https://geek-university.com/python/add-python-to-the-windows-path/)

## Installation 
### For Ubuntu and macOS
- Create virtual environment for python3:
```bash
python3 -m venv env
```

- Activate `env` virtual environment
```bash
source env/bin/activate
```

- Run the following command
```
./start
```

### For Windows
- Create virtual environment for python:
```
python -m venv env
```

- Double click `start.bat`

- Go to localhost:5000 on your preferred browser.


### Assumptions
- Any user can add music (only `.mp3`).
- Any user can delete any songs available on the site.
- Any two or more songs can have same title-artist-album but their URL-slug would be different.
