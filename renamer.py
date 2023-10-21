import os
import random

# Klasör yolunu belirleyin (örneğin, şu anki çalışma dizini)
path = os.path.dirname(os.path.realpath(__file__))

# Klasördeki dosyaları listele
dosya_listesi = os.listdir(path)

for filename in dosya_listesi:
    if os.path.isfile(os.path.join(path, filename)) and filename != "renamer.py":
        # Dosyanın uzantısını alın
        dosya_adi, dosya_uzantisi = os.path.splitext(filename)
        
        # Yeni bir dosya adı oluşturun
        new_filename = str(random.randint(1000000000, 9999999999)) + dosya_uzantisi

        # Dosyayı yeniden adlandırın
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
print("done")