# python
import http.client
import json

# comprehensive dictionary mapping country names to ISO 3166-1 alpha-2 codes
ISO_COUNTRY_CODES = {
    "afghanistan": "AF",
    "albania": "AL",
    "algeria": "DZ",
    "andorra": "AD",
    "angola": "AO",
    "argentina": "AR",
    "armenia": "AM",
    "australia": "AU",
    "austria": "AT",
    "azerbaijan": "AZ",
    "bahamas": "BS",
    "bahrain": "BH",
    "bangladesh": "BD",
    "barbados": "BB",
    "belarus": "BY",
    "belgium": "BE",
    "belize": "BZ",
    "benin": "BJ",
    "bhutan": "BT",
    "bolivia": "BO",
    "bosnia and herzegovina": "BA",
    "botswana": "BW",
    "brazil": "BR",
    "brunei": "BN",
    "bulgaria": "BG",
    "burkina faso": "BF",
    "burundi": "BI",
    "cambodia": "KH",
    "cameroon": "CM",
    "canada": "CA",
    "cape verde": "CV",
    "chile": "CL",
    "china": "CN",
    "colombia": "CO",
    "comoros": "KM",
    "congo": "CG",
    "croatia": "HR",
    "cuba": "CU",
    "cyprus": "CY",
    "czech republic": "CZ",
    "denmark": "DK",
    "djibouti": "DJ",
    "dominica": "DM",
    "dominican republic": "DO",
    "ecuador": "EC",
    "egypt": "EG",
    "el salvador": "SV",
    "equatorial guinea": "GQ",
    "eritrea": "ER",
    "estonia": "EE",
    "eswatini": "SZ",
    "ethiopia": "ET",
    "fiji": "FJ",
    "finland": "FI",
    "france": "FR",
    "gabon": "GA",
    "gambia": "GM",
    "georgia": "GE",
    "germany": "DE",
    "ghana": "GH",
    "greece": "GR",
    "guatemala": "GT",
    "guinea": "GN",
    "guyana": "GY",
    "haiti": "HT",
    "honduras": "HN",
    "hungary": "HU",
    "iceland": "IS",
    "india": "IN",
    "indonesia": "ID",
    "iran": "IR",
    "iraq": "IQ",
    "ireland": "IE",
    "israel": "IL",
    "italy": "IT",
    "jamaica": "JM",
    "japan": "JP",
    "jordan": "JO",
    "kazakhstan": "KZ",
    "kenya": "KE",
    "kiribati": "KI",
    "kuwait": "KW",
    "kyrgyzstan": "KG",
    "laos": "LA",
    "latvia": "LV",
    "lebanon": "LB",
    "lesotho": "LS",
    "liberia": "LR",
    "libya": "LY",
    "lithuania": "LT",
    "luxembourg": "LU",
    "madagascar": "MG",
    "malawi": "MW",
    "malaysia": "MY",
    "maldives": "MV",
    "mali": "ML",
    "malta": "MT",
    "mauritania": "MR",
    "mauritius": "MU",
    "mexico": "MX",
    "moldova": "MD",
    "monaco": "MC",
    "mongolia": "MN",
    "montenegro": "ME",
    "morocco": "MA",
    "mozambique": "MZ",
    "myanmar": "MM",
    "namibia": "NA",
    "nepal": "NP",
    "netherlands": "NL",
    "new zealand": "NZ",
    "nicaragua": "NI",
    "niger": "NE",
    "nigeria": "NG",
    "north korea": "KP",
    "norway": "NO",
    "oman": "OM",
    "pakistan": "PK",
    "panama": "PA",
    "paraguay": "PY",
    "peru": "PE",
    "philippines": "PH",
    "poland": "PL",
    "portugal": "PT",
    "qatar": "QA",
    "romania": "RO",
    "russia": "RU",
    "rwanda": "RW",
    "saudi arabia": "SA",
    "senegal": "SN",
    "serbia": "RS",
    "singapore": "SG",
    "slovakia": "SK",
    "slovenia": "SI",
    "somalia": "SO",
    "south africa": "ZA",
    "south korea": "KR",
    "spain": "ES",
    "sri lanka": "LK",
    "sudan": "SD",
    "sweden": "SE",
    "switzerland": "CH",
    "syria": "SY",
    "taiwan": "TW",
    "tajikistan": "TJ",
    "tanzania": "TZ",
    "thailand": "TH",
    "togo": "TG",
    "tonga": "TO",
    "tunisia": "TN",
    "turkey": "TR",
    "uganda": "UG",
    "ukraine": "UA",
    "united arab emirates": "AE",
    "united kingdom": "UK",
    "united states": "US",
    "uruguay": "UY",
    "uzbekistan": "UZ",
    "venezuela": "VE",
    "vietnam": "VN",
    "yemen": "YE",
    "zambia": "ZM",
    "zimbabwe": "ZW",
}


def get_country_code(country):
    """
    Get the ISO country code for a given country name.

    Args:
        country (str): The name of the country (e.g., 'United Kingdom', 'Canada').

    Returns:
        str: The corresponding ISO country code (e.g., 'UK', 'CA') or None if not found.
    """
    # convert country name to lowercase and retrieve its code from the dictionary
    return ISO_COUNTRY_CODES.get(country.lower())


def get_weather(city, country=None):
    """
    Fetch the current weather data for a specified city using the wttr.in API.

    Args:
        city (str): The name of the city to fetch weather for.
        country (str, optional): The country code (e.g., 'US', 'UK'). Defaults to None.

    Returns:
        dict: A dictionary containing weather information if successful, or None if an error occurs.
    """
    try:
        # construct the query string using the city and optional country code
        query = f"{city},{country}" if country else city

        # establish an HTTPS connection to the wttr.in API
        conn = http.client.HTTPSConnection("wttr.in")

        # send a GET request to fetch weather data in JSON format
        conn.request("GET", f"/{query}?format=j1")
        response = conn.getresponse()

        # check if the response status code indicates success (200 OK)
        if response.status != 200:
            print("Error: Unable to fetch weather data.")
            return None

        # read and parse the JSON response
        data = response.read()
        weather_info = json.loads(data)
        return weather_info

    except Exception as e:
        # handle any exceptions that occur during the request
        print(f"Error: {e}")
        return None

    finally:
        # ensure the connection is closed after the request
        conn.close()


def display_weather(weather, city, country=None):
    """
    Display detailed weather information for the specified city.

    Args:
        weather (dict): The dictionary containing weather information.
        city (str): The name of the city.
        country (str, optional): The country code (e.g., 'US', 'UK'). Defaults to None.
    """
    # check if weather data is available
    if not weather:
        print("No weather information available.")
        return

    # extract the current weather condition from the JSON response
    current_condition = weather["current_condition"][0]

    # extract and store various weather attributes
    temperature = current_condition["temp_C"]
    feels_like = current_condition["FeelsLikeC"]
    description = current_condition["weatherDesc"][0]["value"]
    humidity = current_condition["humidity"]
    wind_speed = current_condition["windspeedKmph"]
    wind_direction = current_condition["winddir16Point"]
    precipitation = float(current_condition["precipMM"])
    pressure = current_condition["pressure"]
    cloud_cover = int(current_condition["cloudcover"])
    visibility = current_condition["visibility"]
    uv_index = current_condition["uvIndex"]

    # format the location with city and optional country code
    location = (
        f"{city.capitalize()}, {country.upper()}" if country else city.capitalize()
    )

    # display the formatted weather information
    print(f"\nWeather in {location}:")
    print(f"Temperature: {temperature}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind: {wind_speed} km/h {wind_direction}")
    print(f"Precipitation: {precipitation} mm")
    print(f"Pressure: {pressure} hPa")
    print(f"Cloud Cover: {cloud_cover}%")
    print(f"Visibility: {visibility} km")
    print(f"UV Index: {uv_index}")


def main():
    """
    Main function to prompt the user for input and display the weather report.
    """
    print("Local Weather Checker")

    city = input("Enter the city: ").strip()

    country = input("Enter the country (name or code, optional): ").strip()

    # convert the country name to its ISO code if provided
    country_code = get_country_code(country) if country else None

    weather = get_weather(city, country_code)
    display_weather(weather, city, country)


if __name__ == "__main__":
    main()
