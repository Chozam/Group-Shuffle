import pandas as pd
import random
import math

# 1.Baca file txt yang per item atau nama dipisahkan oleh \n atau enter
with open("data.txt", "r") as file:
    data = file.readlines()
list_nama = [name.strip() for name in data]


# 2.Loop isi file dan pisahkan menjadi beberapa group banyak nama di file / banyak group
random.shuffle(list_nama)

data_final = {}
list_alih = []

banyak_group = int(input("Mau berapa kelompok: "))
banyak_anggota = math.floor(len(list_nama) / banyak_group)
sisa_anggota = len(list_nama) % banyak_group

for i in range(1, banyak_group + 1):
    data_final[f"group{i}"] = []
    for j in list_nama:
        # try:
        if len(data_final[f"group{i}"]) < banyak_anggota and j not in list_alih:
            data_final[f"group{i}"].append(j)
            list_alih.append(j)
if sisa_anggota > 0:
    for i in range(1, sisa_anggota + 1):
        for j in list_nama:
            if (
                len(data_final[f"group{i}"]) < (banyak_anggota + 1)
                and j not in list_alih
            ):
                data_final[f"group{i}"].append(j)
                list_alih.append(j)
                sisa_anggota -= 1


# 3.Simpan menjadi file csv dan tampilkan
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data_final.items()]))
print(df)
df.to_csv("group_shuffle.csv")
