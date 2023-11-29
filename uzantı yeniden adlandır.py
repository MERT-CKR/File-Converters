import os
print("bu program sadece dosya uzantılarını toplu bir şekilde yeniden adlandırır. yani dosya sistemini değiştirmez.")
format1 = input("değişmesi gereken dosyalarınız hangi formatta ? (örn: .jpg)")
format2 = input("bu formatları ne hangi uzantıya dönüştürmek istersiniz ? (örn: .jpeg)")
def rename_files(input_folder):
    # Giriş klasöründeki tüm jpg dosyalarını al
    jpg_files = [f for f in os.listdir(input_folder) if f.endswith(format1)]

    for jpg_file in jpg_files:
        # Dosya yolu oluştur
        input_path = os.path.join(input_folder, jpg_file)
        
        # Yeni dosya adını oluştur
        gif_file = os.path.splitext(jpg_file)[0] + format2
        output_path = os.path.join(input_folder, gif_file)

        # Dosyayı yeniden adlandır
        os.rename(input_path, output_path)

if __name__ == "__main__":
    input_folder = os.path.dirname(os.path.realpath(__file__))

    rename_files(input_folder)
