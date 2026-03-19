import requests
import pandas as pd

response = requests.get("https://restcountries.com/v3.1/region/oceania")
countries = response.json()

print(f"\nNumber of countries returned: {len(countries)}")
print(f"\nFirst country: {countries[0]['name']['common']}")

data = {
    "country": [c["name"]["common"] for c in countries],
    "population": [c["population"] for c in countries],
    "area": [c["area"] for c in countries],
    "subregion": [c["subregion"] for c in countries]
}

df = pd.DataFrame(data)
print(df)

most_populous = df[df["population"] == df["population"].max()]
total_oceania_population = df["population"].sum()
number_of_countries_in_each_subregion = df["subregion"].value_counts()

print(f"\nTotal oceania population: {total_oceania_population:,}")
print(f"\nMost populous country: {most_populous["country"].values[0]}")
print(f"\nPopulation: {most_populous['population'].values[0]:,}")
print(f"\nNumber of countries in each subregion: {number_of_countries_in_each_subregion}")
