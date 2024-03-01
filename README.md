# Image Stream Hashing Python Script README

## Description
This Python script processes image files in a directory and generates stream hashes using ffmpeg. The resulting stream hash files are saved with the format 'filename_streamhash.txt'.

## Features
- Processes multiple image file formats (e.g., BMP, GIF, JPG, PNG, TIFF)
- Generates stream hashes using ffmpeg
- Saves stream hash files with informative filenames

## Installation
1. Clone this repository to your local machine.
2. Install ffmpeg (use 6.0 or higher version) if you haven't already.


## Usage
To use the script, follow these steps:
1. Place the script in the directory containing the image files you want to process.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the command: `python img_streamh_hashing_batch_script.py`

## Example
Suppose we have the following image files in the c:\tmp directory:
- `example.jpg`
- `sample.png`

Running the script with the following command:
python img_streamh_hashing_batch_script.py

Should produce the following output:

Stream hashing process started...
Processing file: example.jpg
Processing file: sample.png
All stream hashing processes have completed.

After running the script, two stream hash files should be generated:

- `example_streamhash.txt`
- `sample_streamhash.txt`

These text files contain the stream hashes generated for the respective image files.
An example of the text file contents would be something like the following:

0,v,SHA256=dcf481a6a70d0070a6679f6ea3b2587cd790e0a3ec80372ae0c0dac694a69fa8

The entry above is the SHA256 stream hash of the image file.  This is NOT the file container hash.

If you look in the location of the image and text files you should also see a "streamhash_log.txt" file.  

The contents should be something like:
C:\tmp\example.jpg
C:\tmp\sample.png

