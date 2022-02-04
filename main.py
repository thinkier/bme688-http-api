#!/usr/bin/env python3

from bme680 import *
from flask import Flask, jsonify

# How much humidity should contribute to the IAQ score
hum_weight = 0.25
gas_weight = 1 - hum_weight
# The ideal humidity
hum_baseline = 40.0
# Your gas resistance may be different, I've calibrated it against my room while well-ventilated
gas_resistance_baseline = 8e4

sensor = BME680(I2C_ADDR_PRIMARY)

sensor.set_humidity_oversample(OS_2X)
sensor.set_pressure_oversample(OS_2X)
sensor.set_temperature_oversample(OS_2X)
sensor.set_filter(FILTER_SIZE_3)
sensor.set_gas_status(ENABLE_GAS_MEAS)

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

app = Flask(__name__)


@app.route("/report.json")
def report_json():
    if sensor.get_sensor_data():
        data = {
            'temp': sensor.data.temperature,
            'pressure': sensor.data.pressure,
            'humidity': sensor.data.humidity
        }

        if sensor.data.heat_stable:
            data['gas_resistance'] = sensor.data.gas_resistance

            hum_delta = abs(sensor.data.humidity - hum_baseline)
            gas_delta = sensor.data.gas_resistance - gas_resistance_baseline

            air_quality = hum_weight * hum_delta / hum_baseline
            if gas_delta > 0:
                air_quality += gas_weight * gas_delta / gas_resistance_baseline
            else:
                air_quality += gas_weight

            data['air_quality'] = 5 * air_quality

        return jsonify(data)

    return jsonify(), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
