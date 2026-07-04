from weather_etl import(
    create_db_engine,
    get_weather_by_city_name,
    build_city_param,
    get_or_create_city
)

CITIES = ["Incheon",
"Seoul",
"Busan",
"Daejeon",
"Jeonju",
"Daegu",
"Gwangju",
"Ulsan"
]


def main():
    engine = create_db_engine()
    for city in CITIES:
        weather = get_weather_by_city_name(city)
        city_param = build_city_param(weather)

        city_id = get_or_create_city(engine,city_param)
        print(f"{city} -> city_id {city_id}")

if __name__ == "__main__":
    main()