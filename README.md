# bme688-http-api

Expose data from a BME688 chip to an HTTP API.

## Usage

1. Deploy the server using `./main.py`
2. Navigate to `http://YOUR_PI_ADDRESS:5555/report.json`

## Dependencies

- `python3`
- `bme68x` (via [manual installation](https://github.com/pi3g/bme68x-python-library#how-to-install-the-extension-with-bsec))
- `flask` (via pip3)
