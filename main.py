#!/usr/bin/env python3

from bme68x import BME68X
from flask import Flask, jsonify

sensor = BME68X(0x76, 1)
sensor.set_heatr_conf(1, 320, 100, 1)
sensor.get_bsec_data()

app = Flask(__name__)


@app.route("/report.json")
def report_json():
    bsec_data = sensor.get_bsec_data()
    # Output range is 0-500, I want to turn it to 1-5 with consideration for Table 6 at
    # https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme688-ds000.pdf
    air_quality_homekit = (bsec_data.static_iaq / 62.5) + 1

    if air_quality_homekit > 5:
        air_quality_homekit = 5

    data = {
        'temperature': bsec_data.temperature,
        'humidity': bsec_data.humidity,
        'pressure': bsec_data.raw_pressure,
        'air_quality': air_quality_homekit,
        'co2_ppm': bsec_data.co2_equivalent
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
