import os
import imageio

# Geçerli dizini alın
current_directory = os.path.dirname(os.path.realpath(__file__))
webp_files = [file for file in os.listdir(current_directory) if file.endswith(".webp")]

# WebP dosyalarını GIF formatına dönüştürün
for webp_file in webp_files:
    input_file = os.path.join(current_directory, webp_file)
    output_file = os.path.join(current_directory, os.path.splitext(webp_file)[0] + ".gif")
    with imageio.get_reader(input_file) as reader:
        frames = [frame for frame in reader]
    imageio.mimsave(output_file, frames, format="GIF", duration=1, fps =10)  # duration ayarını özelleştirebilirsiniz
print("done")