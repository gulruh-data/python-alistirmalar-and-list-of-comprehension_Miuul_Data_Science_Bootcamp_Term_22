# ==========================================
# PYTHON ALIŞTIRMALAR - TOPLU KODLAR
# ==========================================

# Görev 1: Verilen değerlerin veri yapılarını inceleme
x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
L = [1, 2, 3, 4]
d = {"Name": "Jake", "Age": 27, "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

print("--- GÖREV 1 ÇIKTILARI ---")
for val in [x, y, z, a, b, c, L, d, t, s]:
  print(type(val))

# Görev 2: String metotları uygulamaları
text = "The goal is to turn data into information, and information into insight."
print("\n--- GÖREV 2 ÇIKTISI ---")
print(text.upper().replace(",", "").replace(".", "").split())

# Görev 3: Liste işlemleri
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
print("\n--- GÖREV 3 ÇIKTILARI ---")
print("Eleman sayısı:", len(lst))  # Adım 1
print("0. ve 10. indeks:", lst[0], lst[10])  # Adım 2
sub_lst = lst[0:4]
print("Alt liste (D, A, T, A):", sub_lst)  # Adım 3
# del lst[8]                  # Adım 4 (8. indeksteki elemanı silme)
# lst.append(100)             # Adım 5 (Yeni eleman ekleme)
# lst.insert(8, "N")          # Adım 6 (8. indekse tekrar N ekleme)

# Görev 4: Sözlük (Dictionary) işlemleri
dict_obj = {
    'Christian': ["America", 18],
    'Daisy': ["England", 12],
    'Antonio': ["Spain", 22],
    'Dante': ["Italy", 25],
}
print("\n--- GÖREV 4 ÇIKTILARI ---")
print("Key değerleri:", dict_obj.keys())  # Adım 1
print("Value değerleri:", dict_obj.values())  # Adım 2
dict_obj['Daisy'][1] = 13  # Adım 3
dict_obj['Ahmet'] = ["Turkey", 24]  # Adım 4
del dict_obj['Antonio']  # Adım 5
print("Güncel Sözlük:", dict_obj)

# Görev 5: Tek ve çift sayıları ayıran fonksiyon
l = [2, 13, 18, 93, 22]


def func(lst):
  even_list = [i for i in lst if i % 2 == 0]
  odd_list = [i for i in lst if i % 2 != 0]
  return even_list, odd_list


even, odd = func(l)
print("\n--- GÖREV 5 ÇIKTISI ---")
print("Çiftler:", even, "Tekler:", odd)

# Görev 6: Enumerate kullanarak fakülte sıralaması yazdırma
ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
print("\n--- GÖREV 6 ÇIKTISI ---")
for index, ogr in enumerate(ogrenciler[:3], 1):
  print(f"Mühendislik Fakültesi {index}. öğrenci: {ogr}")
for index, ogr in enumerate(ogrenciler[3:], 1):
  print(f"Tıp Fakültesi {index}. öğrenci: {ogr}")

# Görev 7: Zip kullanarak ders bilgilerini bastırma
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]
print("\n--- GÖREV 7 ÇIKTISI ---")
for kr, kod, kon in zip(kredi, ders_kodu, kontenjan):
  print(f"Kredisi {kr} olan {kod} kodlu dersin kontenjanı {kon} kişidir.")

# Görev 8: Set (Küme) operasyonları fonksiyonu
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume_analiz(k1, k2):
  if k1.issuperset(k2):
    return k1.intersection(k2)
  else:
    return k2.difference(k1)


print("\n--- GÖREV 8 ÇIKTISI ---")
print("Küme Sonucu:", kume_analiz(kume1, kume2))

# ==========================================
# LIST COMPREHENSION ALIŞTIRMALAR
# ==========================================
import seaborn as sns

df = sns.load_dataset("car_crashes")

# Görev 1: Numeric değişken isimlerini büyük harfe çevirip başına NUM ekleme[cite: 16]
df.columns = [
    "NUM_" + col.upper() if "NUM" not in col.upper() else col.upper()
    for col in df.columns
]
print("Görev 1 Çıktısı:", df.columns)

# Yeniden orijinal dataframe'i yükleyelim ki sonraki görevler etkilenmesin
df = sns.load_dataset("car_crashes")

# Görev 2: İsmi "no" barındırmayanların sonuna FLAG ekleme, tümünü büyütme[cite: 17]
df.columns = [
    col.upper() + "_FLAG" if "NO" not in col.upper() else col.upper()
    for col in df.columns
]
print("Görev 2 Çıktısı:", df.columns)

# Görev 3: Belirli değişkenleri hariç tutarak yeni dataframe oluşturma[cite: 18]
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print("Görev 3 Yeni DataFrame İlk 5 Satır:\n", new_df.head())