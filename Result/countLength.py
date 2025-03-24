import pandas as pd

df1 = pd.read_json("./Provinsi_Jakarta.json")
# df2 = pd.read_json("./Provinsi_JawaBarat2.json")
# df3 = pd.read_json("./Provinsi_JawaBarat3.json")
# df4 = pd.read_json("./Provinsi_Banten4.json")


print(len(df1) )
# df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# df.to_json("FixProvinsi_JawaBarat.json", orient="records")