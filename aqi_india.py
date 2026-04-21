def calculate_aqi_pm25_india(concentration):

    breakpoints = [
        (0, 30, 0, 50),
        (31, 60, 51, 100),
        (61, 90, 101, 200),
        (91, 120, 201, 300),
        (121, 250, 301, 400),
        (251, 500, 401, 500),
    ]

    for Clow, Chigh, Ilow, Ihigh in breakpoints:

        if Clow <= concentration <= Chigh:

            aqi = ((Ihigh - Ilow) / (Chigh - Clow)) * (concentration - Clow) + Ilow

            return round(aqi)

    return None


def get_category_india(aqi):

    if aqi is None:
        return "No Data"

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Satisfactory"

    elif aqi <= 200:
        return "Moderate"

    elif aqi <= 300:
        return "Poor"

    elif aqi <= 400:
        return "Very Poor"

    else:
        return "Severe"