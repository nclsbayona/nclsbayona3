# coding: utf-8
from asyncio import get_event_loop
from base64 import b64encode
from os import environ
from random import choice, randint
from typing import Dict, List

from chevron.renderer import render
from prettytable import PrettyTable
from requests import get
from requests.models import Response

# nclsbayona


async def getDrink(format="string") -> Dict[str, str]:
    """Gets a random drink information from The Cocktail DB API"""
    try:
        the_response: Response = get(
            "https://www.thecocktaildb.com/api/json/v1/1/random.php"
        )
        table_drink: PrettyTable = PrettyTable(["Ingredient", "Measure"])
        response: Dict[str, str] = the_response.json().get("drinks")[0]
        drink: Dict[str, str] = dict()
        drink["drink_name"] = response["strDrink"]
        drink["drink_alcoholic_category"] = response["strAlcoholic"]
        drink["drink_category"] = response["strCategory"]
        drink["drink_instructions"] = response["strInstructions"]
        drink["drink_image"] = response["strDrinkThumb"]
        ingredients: List[str] = list()
        quantities: List[str] = list()
        for key in response:
            if response[key] is not None:
                if key.count("Ingredient") > 0:
                    ingredients.append(response[key])

                elif key.count("Measure") > 0:
                    quantities.append(response[key])

        tot: int = len(quantities)
        for i in range(tot):
            table_drink.add_row([ingredients[i], quantities[i]])

        if format == "string":
            drink["table_drink"] = table_drink.get_string(format=True)
        elif format == "html":
            drink["table_drink"] = table_drink.get_html_string(format=True)
        elif format == "json":
            drink["table_drink"] = table_drink.get_json_string(format=True)
        elif format == "csv":
            drink["table_drink"] = table_drink.get_csv_string(format=True)

        return drink

    except Exception or KeyboardInterrupt:
        return {"error_msj": "An error ocurred please try again"}


async def getAffirmation() -> Dict[str, str]:
    """Gets a translated text from an quote to a random pop character language from funtranslations API"""
    try:
        characters: List[str] = [
            "pirate",
            "minion",
            "sindarin",
            "oldenglish",
            "ferblatin",
            "dothraki",
            "valyrian",
            "vulcan",
            "klingon",
            "pig-latin",
            "yoda",
            "sith",
            "cheunh",
            "gungan",
            "mandalorian",
            "huttese",
        ]
        # Be sure it's a random choice
        translate_to: str = choice(characters)
        #
        choices: int = randint(1, 3)
        response: Response = None
        affirmation: str = None
        if choices == 1:
            response = get("https://affirmations.dev")
            affirmation = (response.json()).get("affirmation")

        elif choices == 2:
            response = get("https://zenquotes.io/api/random")
            affirmation = (response.json())[0].get("q")

        elif choices == 3:
            response = get("https://quotes.rest/qod.json?language=en")
            affirmation = (
                (response.json()).get("contents").get("quotes")[0].get("quote")
            )

        del choices
        text: str = affirmation
        response = get(
            f"https://api.funtranslations.com/translate/{translate_to}.json?text={affirmation}"
        )
        affirmation = (response.json()).get("contents").get("translated")
        affirmation = f"The text '{text}' was translated to {translate_to} language, and the result is: '{affirmation}'"

        new_dictionary: Dict[str, str] = dict()
        new_dictionary["text_affirmation"] = affirmation

        if translate_to == "yoda":
            new_dictionary[
                "affirmation_image"
            ] = "https://tukaramatthews.com/wp-content/uploads/2015/03/FullSizeRender.jpg"
        elif translate_to == "pirate":
            new_dictionary[
                "affirmation_image"
            ] = "https://image.flaticon.com/icons/png/512/287/287744.png"
        elif translate_to == "minion":
            new_dictionary[
                "affirmation_image"
            ] = "https://4.bp.blogspot.com/-kLGmroF-doI/VeJhCJlpeyI/AAAAAAAASK4/TRvjlSKu4nk/s1600/13.jpeg"
        elif translate_to == "sindarin":
            new_dictionary[
                "affirmation_image"
            ] = "https://i.etsystatic.com/8273882/r/il/c6deb3/475904358/il_570xN.475904358_enru.jpg"
        elif translate_to == "oldenglish":
            new_dictionary[
                "affirmation_image"
            ] = "https://i.etsystatic.com/21833494/r/il/7e76dd/2140080884/il_570xN.2140080884_ikw0.jpg"
        elif translate_to == "ferblatin":
            new_dictionary[
                "affirmation_image"
            ] = "https://i.ytimg.com/vi/I3nAGsT2skc/maxresdefault.jpg"
        elif translate_to == "dothraki":
            new_dictionary[
                "affirmation_image"
            ] = "https://www.trbimg.com/img-55791e95/turbine/la-oe-0611-peterson-game-of-thrones-dothraki-20150611"
        elif translate_to == "valyrian":
            new_dictionary[
                "affirmation_image"
            ] = "https://www.theverge.com/tldr/2017/7/11/15952124/game-of-thrones-high-valyrian-language-course-app"
        elif translate_to == "vulcan":
            new_dictionary[
                "affirmation_image"
            ] = "https://geneticliteracyproject.org/wp-content/uploads/2017/01/Leonard-Nimoy.png"
        elif translate_to == "klingon":
            new_dictionary[
                "affirmation_image"
            ] = "https://static.independent.co.uk/s3fs-public/thumbnails/image/2016/03/14/19/9-klingon-star-trek.jpg"
        elif translate_to == "pig-latin":
            new_dictionary[
                "affirmation_image"
            ] = "https://www.quickanddirtytips.com/sites/default/files/images/2104/piglatin.jpg"
        elif translate_to == "sith":
            new_dictionary["affirmation_image"] = "https://i.redd.it/ra6s480wfi701.jpg"
        elif translate_to == "cheunh":
            new_dictionary[
                "affirmation_image"
            ] = "https://www.thathashtagshow.com/wp-content/uploads/2019/07/steadfast-1024x655.jpg"
        elif translate_to == "gungan":
            new_dictionary[
                "affirmation_image"
            ] = "https://img1.wikia.nocookie.net/__cb20091012212518/aliens/images/9/93/Gungan-Otolla.jpg"
        elif translate_to == "mandalorian":
            new_dictionary[
                "affirmation_image"
            ] = "https://cdn.dribbble.com/users/2110632/screenshots/5607696/dribbble-03_2x.png"
        elif translate_to == "huttese":
            new_dictionary["affirmation_image"] = "https://rb.gy/vu0j2o"

        return new_dictionary

    except Exception or KeyboardInterrupt:
        return {"text_affirmation": "An error ocurred please try again later"}


async def getWeather(query: str = None, key: str = None) -> Dict[str, str]:
    """Gets the weather information from OPENWEATHER API using a query and a key specified by the user"""
    try:
        query = environ["THE_CITY"] if query is None else query
        key = environ["OPEN_WEATHER_MAP_KEY"] if key is None else key
        response = get(
            f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={key}&units=metric"
        )
        the_response: Dict[str, str] = response.json()
        dictionary: Dict[str, str] = dict()
        dictionary["city_temperature"] = str(the_response["main"]["temp"])
        dictionary["city_min_temperature"] = str(the_response["main"]["temp_min"]) + "°C"
        dictionary["city_max_temperature"] = str(the_response["main"]["temp_max"]) + "°C"
        dictionary["city_termic_sensation"] = str(the_response["main"]["feels_like"]) + "°C"
        dictionary["city_pressure"] = str(the_response["main"]["pressure"]) + "Pa"
        dictionary["city_weather"] = the_response["weather"][0]["description"]

        return dictionary

    except Exception or KeyboardInterrupt:
        return {"error_msj": "An error ocurred please verify your inputs and try again"}


async def getWakaStats(waka_key: str = None, format: str = "string") -> Dict[str, str]:
    """Gets WAKATIME API data, and returns in a dictionary some of the information"""
    try:
        dictionary: Dict[str, str] = dict()
        encoded_key: str = str(b64encode(waka_key.encode("utf-8")), "utf-8")
        wakatime_data: Dict = get(
            "https://wakatime.com/api/v1/users/current/stats/last_7_days",
            headers={"Authorization": f"Basic {encoded_key}"},
        ).json()

        # Tables
        table_languages: PrettyTable = PrettyTable(["Language name", "Time spent"])
        temp_list: List[str] = list()
        coded_on: List[Dict[str, str]] = wakatime_data["data"]["languages"]
        for language in coded_on:
            temp_list.clear()
            temp_list.append(language["name"])
            temp_list.append("{hours} hours and {minutes} minutes".format(**language))
            table_languages.add_row(temp_list.copy())

        table_os: PrettyTable = PrettyTable(["OS name", "Time spent"])
        coded_on = wakatime_data["data"]["operating_systems"]

        for os in coded_on:
            temp_list.clear()
            temp_list.append(os["name"])
            temp_list.append("{hours} hours and {minutes} minutes".format(**os))
            table_os.add_row(temp_list.copy())

        if format == "string":
            dictionary["languages"] = table_languages.get_string(format=True)
            dictionary["coded_on_os"] = table_os.get_string(format=True)
        elif format == "html":
            dictionary["languages"] = table_languages.get_html_string(format=True)
            dictionary["coded_on_os"] = table_os.get_html_string(format=True)
        elif format == "json":
            dictionary["languages"] = table_languages.get_json_string(format=True)
            dictionary["coded_on_os"] = table_os.get_json_string(format=True)
        elif format == "csv":
            dictionary["languages"] = table_languages.get_csv_string(format=True)
            dictionary["coded_on_os"] = table_os.get_csv_string(format=True)

        del temp_list, table_os, table_languages
        return dictionary

    except Exception or KeyboardInterrupt:
        return {"error_msj": "An error ocurred please verify your inputs and try again"}


async def getAll(
    open_weather_query: str = None,
    open_weather_key: str = None,
    waka_time_api_key: str = None,
    format: str = "string",
) -> Dict[str, str]:
    """Gets the information gathered using the rest of the functions"""
    try:
        drink = await getDrink(format=format)
        affirmation = await getAffirmation()
        weather = await getWeather(query=open_weather_query, key=open_weather_key)
        waka = await getWakaStats(waka_key=waka_time_api_key, format=format)
        print(drink, affirmation, weather, waka)
        dictionary: Dict[str, str] = {**drink, **affirmation, **weather, **waka}
        return dictionary
    except Exception or KeyboardInterrupt:
        return {"error_msj": "Error ocurred"}


if __name__ == "__main__":

    async def updateFile(
        path_to_new_file: str = "README.md",
        path_to_template_file: str = "directory_file",
        open_weather_query: str = None,
        open_weather_key: str = None,
        waka_time_api_key: str = None,
        format: str = "string",
    ) -> bool:
        """Updates a file with the information gathered using the rest of the functions"""
        try:
            dictionary = await getAll(
                open_weather_query=open_weather_query,
                open_weather_key=open_weather_key,
                waka_time_api_key=waka_time_api_key,
                format=format,
            )
            print("The dictionary\n", dictionary)
            with (open(path_to_template_file, "r")) as template_file:
                with (open(path_to_new_file, "w")) as new_file:
                    new_file.write(render(template_file, dictionary))
            return True
        except Exception or KeyboardInterrupt:
            return False

    async def main(open_weather_query, open_weather_key, waka_time_api_key, format):
        await updateFile(
            open_weather_query=open_weather_query,
            open_weather_key=open_weather_key,
            waka_time_api_key=waka_time_api_key,
            format=format,
        )

    waka_api_key = environ["WAKATIME_API_KEY"]
    open_weather_key = environ["OPEN_WEATHER_MAP_KEY"]
    open_weather_query = environ["LOCATION"]
    format = "html"
    loop = get_event_loop()
    loop.run_until_complete(
        main(
            open_weather_query=open_weather_query,
            open_weather_key=open_weather_key,
            waka_time_api_key=waka_api_key,
            format=format,
        )
    )
    loop.close()
