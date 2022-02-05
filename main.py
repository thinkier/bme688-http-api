#!/usr/bin/env python3

from time import sleep

import bsecConstants as bsec
from bme68x import BME68X
from flask import Flask, jsonify

sensor = BME68X(0x76, 0)
sensor.set_sample_rate(bsec.BSEC_SAMPLE_RATE_LP)

app = Flask(__name__)


# Derived from https://github.com/pi3g/bme68x-python-library/blob/main/examples/airquality.py
# MIT Licensed (c) 2021 Pi3g
def get_data(s):
    data = {}
    try:
        data = s.get_bsec_data()
    except Exception as e:
        print(e)
        return None
    if data is None or data == {}:
        sleep(0.1)
        return None
    else:
        sleep(3)
        return data


@app.route("/report.json")
def report_json():
    bsec_data = None
    while bsec_data is None:
        bsec_data = get_data(sensor)

    # Output range is 0-500, I want to turn it to 1-5 with consideration for Table 6 at
    # https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme688-ds000.pdf
    air_quality_homekit = (bsec_data['static_iaq'] / 62.5) + 1

    if air_quality_homekit > 5:
        air_quality_homekit = 5

    data = {
        'temperature': bsec_data['temperature'],
        'humidity': bsec_data['humidity'],
        'pressure': bsec_data['raw_pressure'],
        'air_quality': air_quality_homekit,
        'co2_ppm': bsec_data['co2_equivalent'],
        'voc_ppm': bsec_data['breath_voc_equivalent']
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
