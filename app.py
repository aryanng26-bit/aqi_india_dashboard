from flask import Flask, render_template, request
import pandas as pd

from aqi_india import calculate_aqi_pm25_india, get_category_india

app = Flask(__name__)

# Load dataset safely
data = pd.read_csv("data.csv")
data.columns = data.columns.str.strip().str.lower()  # FIXES column issues


def get_city_aqi(city):

    row = data[data["city"].str.lower() == city.lower()]

    if not row.empty:
        pm25 = float(row.iloc[0]["pm25"])
        pm10 = float(row.iloc[0]["pm10"])
        no2 = float(row.iloc[0]["no2"])

        aqi = calculate_aqi_pm25_india(pm25)
        category = get_category_india(aqi)

        return pm25, pm10, no2, aqi, category

    return None, None, None, None, "City Not Found"


@app.route("/", methods=["GET", "POST"])
def index():

    results = []

    if request.method == "POST":

        cities = request.form.getlist("cities")

        for city in cities:

            pm25, pm10, no2, aqi, category = get_city_aqi(city)

            results.append({
                "city": city,
                "pm25": pm25 if pm25 else "N/A",
                "pm10": pm10 if pm10 else "N/A",
                "no2": no2 if no2 else "N/A",
                "aqi": aqi if aqi else "N/A",
                "category": category
            })

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)