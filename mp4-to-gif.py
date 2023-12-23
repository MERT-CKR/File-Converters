import subprocess
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
mp4_files = [file for file in os.listdir(current_directory) if file.endswith(".mp4")]

for mp4_file in mp4_files:
    input_file = os.path.join(current_directory, mp4_file)
    output_file = os.path.join(current_directory, os.path.splitext(mp4_file)[0] + ".gif")

    # Bit hızını 2000k'ya, kalite seviyesini 1'e ayarla
    ffmpeg_command = f'ffmpeg -i "{input_file}" -vf "fps=10,scale=640:-1" -c:v gif -b:v 2000k -q:v 1 "{output_file}"'
    subprocess.run(ffmpeg_command, shell=True)

    print(f"Conversion of {input_file} completed")

print("done")
