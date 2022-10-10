import pandas as pd


def use_pandas():
    '''
    Try some pandas functions for pynguin test reasons.:
    '''
    df = pd.DataFrame({
        "My_Data": [3, 4, 5],
        "My_age": [9000, 4, 90],
        "My_Name": ["Test", "Manfred", "Herbert"]
    }, index=[1, 2, 3])

    df_copy = df.copy()
    df_copy["My_age"] = df_copy["My_age"].apply(func=lambda x: x * x)
    df_copy.to_csv("./my_comma_separated_value_file.csv", index=False)

