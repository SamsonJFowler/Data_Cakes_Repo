import pandas as pd

# make a dataframe into a csv file,
dt = {
    "ID": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
    ],
    "first_name": [
        "ian",
        "barbara",
        "susan",
        "jamie",
        "victoria",
        "zoe",
        "liz",
        "sarah",
        "harry",
        "mel",
        "grace",
        "rose",
    ],
    "resiidency": [
        "london",
        "london",
        "'london'",
        "Scotland",
        "England",
        "England",
        "England",
        "aberdden",
        "london",
        "Pease pottage",
        "san francisco",
        "london",
    ],
    "tenuure": [
        63,
        63,
        63,
        66,
        67,
        68,
        70,
        73,
        74,
        86,
        96,
        5,
    ],
}
mydt = pd.DataFrame(
    dt,
    columns=[
        "ID",
        "first_name",
        "resiidency",
        "tenuure",
    ],
)

mydt.to_csv(
    "~\\code\\Data_Cakes_Repo\\data\\sample_1.csv",
    encoding="utf-8",
    sep="\t",
)


# %%
