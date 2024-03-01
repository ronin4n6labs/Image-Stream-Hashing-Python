"""

Script:  img_stream_hashing_batch_script.py

Description:
 This script processes image files in the same directory and generates streamhash for each image using ffmpeg.
 The files extensions this script processes include .bmp, .gif, .jpg, .png, and .tif.
 The resulting streamhash files are saved with the format 'filename_streamhash.txt."
 In addition, the script creates a streamhash_log.txt file for each file it processes.

Usage:
 Place this script in the directory containing the image files you want to process, then run the script.

Script authored by Gregory S. Wales, DFS
For more information or collaboration opportunities, visit: https://github.com/ronin4n6labs

References:
 1. Wales GS, Smith JM, Lacey DS,Grigoras C. "Multimedia stream hashing: A forensic method for
    content verification."" J Forensic Sci. 2023;68:289–300. https://doi.org/10.1111/1556-4029.15148

 2. Wales GS. "Validation of image stream hashing: A forensic method for content verification."
    J Forensic Sci. 2023;00:1–14. https://doi.org/10.1111/1556-4029.15432

Licensing:
 This script is licensed under the MIT License.
 For more information, see the LICENSE file or visit:
 https://opensource.org/licenses/MIT

###############################################################################################

"""

import os
import subprocess

# Function to execute ffmpeg command
def execute_ffmpeg(input_file, output_file, log_file):
    command = ['ffmpeg', '-i', input_file, '-f', 'streamhash', '-']
    with open(output_file, 'w') as f:
        subprocess.run(command, stdout=f, stderr=subprocess.PIPE)
        # Write filename and extension to log file
        log_file.write(f"{input_file}\n")

# Print message indicating the start of the stream hashing process
print("Stream hashing process started...")

# Get the path to the folder containing the script
script_folder = os.path.dirname(os.path.abspath(__file__))

# Open log file for writing
log_file_path = os.path.join(script_folder, "streamhash_log.txt")
with open(log_file_path, "w") as log_file:
    # Iterate through files in the folder
    for filename in os.listdir(script_folder):
        if filename.endswith(('.bmp', '.gif', '.jpg', '.png', '.tif')):
            input_file = os.path.join(script_folder, filename)
            output_file = os.path.join(script_folder, f"{os.path.splitext(filename)[0]}_streamhash.txt")
            execute_ffmpeg(input_file, output_file, log_file)

# Print message indicating the completion of the stream hashing process
print("All stream hashing processes have completed.")

# Close log file
log_file.close()
