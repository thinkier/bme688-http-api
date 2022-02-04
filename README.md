# bme688-http-api
Expose data from a BME688 chip to an HTTP API.

## Usage
- `docker-compose up` if you have docker on a Pi 4B (which this was tested against)
  - Doesn't work on my Pi Zero W (gen 1) via docker
- `chmod +x main.py; ./main.py` if you have the dependencies installed via pip3

## Dependencies
- `python3`
- `bme680` (via pip3)
- `flask` (via pip3)
