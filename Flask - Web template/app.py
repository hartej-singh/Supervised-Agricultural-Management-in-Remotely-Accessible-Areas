import joblib
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from datetime import datetime
import math

from keras.models import load_model

sc = joblib.load(r"D:\VIT\Semester-5\B1 CSE3009 (IoT)\Project\R3\Web template\models\scaler")
sc2 = joblib.load(r"D:\VIT\Semester-5\B1 CSE3009 (IoT)\Project\R3\Web template\models\scaler2")
model_h = load_model(r"D:\VIT\Semester-5\B1 CSE3009 (IoT)\Project\R3\Web template\models\RNNmodel-Humidity.h5")
model_t = load_model(r"D:\VIT\Semester-5\B1 CSE3009 (IoT)\Project\R3\Web template\models\RNNmodel-Temperature.h5")
app = Flask(__name__)

dataset = pd.read_csv(r"D:\VIT\Semester-5\B1 CSE3009 (IoT)\Project\archive\iot_telemetry_data.csv")


def Sat_press(Tdb):
    # Function to compute saturation vapor pressure in [kPa]

    C1 = -5674.5359
    C2 = 6.3925247
    C3 = -0.009677843
    C4 = 0.00000062215701
    C5 = 2.0747825E-09
    C6 = -9.484024E-13
    C7 = 4.1635019
    C8 = -5800.2206
    C9 = 1.3914993
    C10 = -0.048640239
    C11 = 0.000041764768
    C12 = -0.000000014452093
    C13 = 6.5459673

    TK = Tdb + 273.15

    if TK <= 273.15:
        result = math.exp(C1 / TK + C2 + C3 * TK + C4 * TK ** 2 + C5 * TK ** 3 +
                          C6 * TK ** 4 + C7 * math.log(TK)) / 1000
    else:
        result = math.exp(C8 / TK + C9 + C10 * TK + C11 * TK ** 2 + C12 * TK ** 3 +
                          C13 * math.log(TK)) / 1000
    return result


def Hum_rat2(Tdb, RH, P):
    Pws = Sat_press(Tdb)
    result = 0.62198 * RH * Pws / (P - RH * Pws)
    return result


def den(P, T, RH):
    P = P / 1000
    # p1 = 6.1078 * 10 ^ [7.5 * T / (T + 237.3)]
    p1 = 6.1078 * (math.pow(10, (7.5 * T / (T + 237.3))))
    pv = p1 * RH
    pd = P - pv
    T = T + 273.15
    result = (pd / (287.058 * T)) + (pv / (461.495 * T))
    return result


def psych(P, in0Val, in1Val):
    P = P / 1000
    Tdb = in0Val
    RH = in1Val
    W = Hum_rat2(Tdb, RH, P)
    outVal = W
    return outVal


@app.route('/', methods=["POST", "GET"])
def start():
    day = 31
    data_h = []
    data_t = []
    for i in range(day - 29, day + 1):
        data_h.append(dataset.humidity[i])
        data_t.append(dataset.temp[i])
    data_h = np.array(data_h)
    data_h = data_h.reshape(-1, 1)
    data_h = sc.fit_transform(data_h)
    data_h = np.reshape(data_h, (1, 30, 1))
    y_data_h = model_h.predict([data_h])
    y_data_h = sc.inverse_transform(y_data_h)
    data_t = np.array(data_t)
    data_t = data_t.reshape(-1, 1)
    data_t = sc2.fit_transform(data_t)
    data_t = np.reshape(data_t, (1, 30, 1))
    y_data_t = model_h.predict([data_t])
    y_data_t = sc.inverse_transform(y_data_t)
    P = 101325
    T = y_data_t
    RH = y_data_h / 100
    x2 = psych(float(P), float(T), float(RH))
    Tf = 25
    RHf = 0.5
    x1 = psych(float(P), float(Tf), float(RHf))
    density = den(float(P), float(T), float(RH))
    volume = 937.5
    load = volume * density * abs(x1 - x2)
    e = 60 * load

    if request.method == "POST":
        day = request.form["days"]
        day = int(day)
        data_h = []
        data_t = []
        for i in range(day - 29, day + 1):
            data_h.append(dataset.humidity[i])
            data_t.append(dataset.temp[i])
        data_h = np.array(data_h)
        data_h = data_h.reshape(-1, 1)
        data_h = sc.fit_transform(data_h)
        data_h = np.reshape(data_h, (1, 30, 1))
        y_data_h = model_h.predict([data_h])
        y_data_h = sc.inverse_transform(y_data_h)
        data_t = np.array(data_t)
        data_t = data_t.reshape(-1, 1)
        data_t = sc2.fit_transform(data_t)
        data_t = np.reshape(data_t, (1, 30, 1))
        y_data_t = model_h.predict([data_t])
        y_data_t = sc.inverse_transform(y_data_t)
        P = 101325
        T = y_data_t
        RH = y_data_h / 100
        x2 = psych(float(P), float(T), float(RH))
        Tf = 25
        RHf = 0.5
        x1 = psych(float(P), float(Tf), float(RHf))
        density = den(float(P), float(T), float(RH))
        volume = 937.5
        load = volume * density * abs(x1 - x2)
        e = 60 * load
        # date_time = datetime.datetime.fromtimestamp( epoch_time )

        # threshold_energy = request.form["threshold_energy"]
        # threshold_energy = int(threshold_energy)
        # threshold_energy = 24
        # remaining_energy = 30
        # calculated_energy = remaining_energy - e
        # flag = 0
        # if y_data_h > 65:
        #     text = "Energy is less than threshold! Please refuel the generator."
        #     flag = 1
        # else:
        #     text = f"Sufficient energy is remaining."
        # remaining_energy = calculated_energy

        return render_template("index.html", date=datetime.fromtimestamp(dataset.ts[day]),
                               co=round(dataset.co[day], 5), humidity=round(dataset.humidity[day], 5),
                               light=dataset.light[day],
                               lpg=round(dataset.lpg[day], 5), motion=dataset.motion[day],
                               smoke=round(dataset.smoke[day], 5), temp=round(dataset.temp[day], 5),
                               y_data=y_data_h[0][0], energy=round(e, 5), day_selected=day) #, flag=flag, text=text)

    return render_template("index.html", date=datetime.fromtimestamp(dataset.ts[day]),
                           co=round(dataset.co[day], 5), humidity=round(dataset.humidity[day], 5),
                           light=dataset.light[day],
                           lpg=round(dataset.lpg[day], 5), motion=dataset.motion[day],
                           smoke=round(dataset.smoke[day], 5), temp=round(dataset.temp[day], 5),
                           y_data=y_data_h[0][0], energy=round(e, 5), day_selected=day)


if __name__ == '__main__':
    app.run(debug=True)
