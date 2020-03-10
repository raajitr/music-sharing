## Music Streamer/Sharer/Management Mock Website

### Prequisites
- Python 3.7+

### Installation
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

### Assumptions
- Any user can add music (only `.mp3`).
- Any user can delete any songs available on the site.
- Any two or more songs can have same title-artist-album but their URL-slug would be different.
