# bme688-http-api
Expose data from a BME688 chip to an HTTP API.

## Usage
1. Deploy the server, this can be done via 2 methods
  - `docker-compose up` if you have docker on a Pi 4B (which this was tested against)
    - Doesn't work on my Pi Zero W (gen 1) via docker
  - `chmod +x main.py; ./main.py` if you have the dependencies installed via pip3
2. Navigate to `http://YOUR_PI_ADDRESS:5555/report.json`

## Dependencies
- `python3`
- `bme680` (via pip3)
- `flask` (via pip3)
