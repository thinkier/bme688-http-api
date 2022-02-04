#!/usr/bin/env python3

from flask import Flask, jsonify
from bme680 import *

sensor = BME680(I2C_ADDR_PRIMARY)

sensor.set_humidity_oversample(OS_2X)
sensor.set_pressure_oversample(OS_2X)
sensor.set_temperature_oversample(OS_2X)
sensor.set_filter(FILTER_SIZE_3)


app = Flask(__name__)

@app.route("/report.json")
def report_json():
    sensor.get_sensor_data()
    data = {
        'temp': sensor.data.temperature,
        'pressure': sensor.data.pressure,
        'humidity': sensor.data.humidity
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5555')
