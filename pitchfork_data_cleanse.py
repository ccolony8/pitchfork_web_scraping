import pandas as pd
import datetime as dt

#read albums part 1 csv file

albums_part1 = pd.read_csv("C:/Users/Charlie Colony/Desktop/albums_part1.csv", delimiter="|")
albums_part1.columns = ['Album','Artist','Pitchfork Score','Pitchfork Author','Genre','Review Date']

#strip Review Date values and change data types
albums_part1["Review Date"] = albums_part1["Review Date"].str.split("T").str.get(0)
albums_part1["Review Date"] = pd.to_datetime(albums_part1["Review Date"])
albums_part1["Genre"] = albums_part1["Genre"].astype("category")

len(albums_part1.head())

# read albums part 2 csv file
albums_part2 = pd.read_csv("C:/Users/Charlie Colony/Desktop/albums_part2.csv", delimiter="|")
albums_part2.columns = ['Album','Artist','Pitchfork Score','Pitchfork Author','Genre','Review Date']

#strip Review Date values and change data types
albums_part2["Review Date"] = albums_part2["Review Date"].str.split("T").str.get(0)
albums_part2["Review Date"] = pd.to_datetime(albums_part1["Review Date"])
albums_part2["Genre"] = albums_part2["Genre"].astype("category")

#concatenate the two csv files
albums_complete = pd.concat([albums_part1, albums_part2], ignore_index=False)

#export to new csv file
albums_complete.to_csv("C:/Users/Charlie Colony/Desktop/albums_complete.csv", sep="|", encoding="utf-8", index=False)