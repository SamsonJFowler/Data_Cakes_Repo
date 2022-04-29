# %% import statements
import pandas as pd
import os

os.getcwd()


# TODO - get a file

# data dir
data = (
    "~\\code\\Data_Cakes_Repo\\data\\"
)


# %%
# TODO - read a csv
df = pd.read_csv(f"{data}sample.csv")

df
# %% read csv - encoding, usually taken care
df = pd.read_csv(
    f"{data}sample.csv",
    encoding="latin-1",
)
df
# %% read csv - seps - setting default seperators,
df = pd.read_csv(
    f"{data}sample.csv",
    encoding="utf-8",
    sep="\t",
)
df
# %% - read csv - tsv files - sep= 't'
df = pd.read_csv(
    f"{data}sample.csv",
    encoding="utf-8",
    sep=",",
    header=0,
)
df

# %%
# TODO - read csv - setting index column,
df = pd.read_csv(
    f"{data}sample.csv",
    encoding="utf-8",
    sep=",",
    header=1,
    index_col=0,
)
df

# %%

# TODO - read csv - setting head parameter, if you want to use a specifc row for your header,
df = pd.read_csv(
    f"{data}sample.csv",
    encoding="utf-8",
    sep=",",
    header=1,
    index_col="ID",
)
df

# %%
# - how to deal with unmwanted columns,
df.drop(
    df.columns[
        df.columns.str.contains(
            "unnamed", case=False
        )  # str. functions are a whole session in themselves,
    ],
    axis=1,  # specifies columns
    inplace=True,  # we don't have to reasign
)
df
# %%
# TODO - drop empty columns, is neat, but won't work here.
df.dropna(
    how="all",
    axis="columns",
    inplace=True,
)

# %%
# just don't import it when you read in the file.
# TODO - read csv - read in only certain columns
cols = [
    "ID",
    "first_name",
    "resiidency",
    "tenuure",
]

df = pd.read_csv(
    f"{data}sample_1.csv",
    names=cols,
    header=None,
    skiprows=1,
    sep="\t",
).set_index("ID")

df


# 0 index, will use the second row of the spreadsheet,


# %%
# TODO - useing usecols and nrows, to slice particualr sections out of csvs
mydata08 = pd.read_csv(
    "http://winterolympicsmedals.com/medals.csv",
    usecols=[1, 5, 7],
    nrows=5,
)
mydata08

# %%


# TODO - read csv - rename columns

# TODO - read csv - WORD OF CAUTION, panda series, if you read in a single column, and you use this squeeze
df = pd.read_csv(
    "aug_train.csv",
    usecols=["gender"],
    squeeze=True,
)
df


# TODO - read csv - skiprows
df = pd.read_csv()
df
# TODO - read csv - nrows, when you have a lot of time,


# TODO - read large files,


# how to do bad thigns
# TODO - read csv - error bad lines paramters,
# If we have a dataset in which some lines is having too many fields (For Example, a CSV line with too many commas), then by default it raises and causes an exception, and no DataFrame will be returned.

# So, to resolve these types of issues we have to make this parameter False, then these “bad lines” will be dropped from the DataFrame that is returned. (Only valid with C parser)
#
# TODO - read csv - parse dates

# TODO - read csv - passing custom function at read in, using converters


def rename(name):
    if (
        name
        == "Royal Challengers Bangalore"
    ):
        return "RCB"
    else:
        return name


pd.read_csv(
    "samples.csv",
    converters={"resiidency": rename},
)

# TODO - read csv - change default null values
# As we know that, the default missing values will be NaN. If we want other strings to be considered as NaN, then we have to use this parameter. It expects a list of strings as the input.

# Sometimes in our dataset, another type of symbol is used to make them missing values, so at that time to understand those values as missing, we use this parameter.
pd.read_csv(
    "sample.csv", na_values=["Null",]
)


# TODO - working with an excel file,


# TODO - read csv - opening a csv file from a url,

# TODO - read excel
# TODO - read sheets
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO
# TODO

# %%
