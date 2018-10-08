# Python Image Extractor

This project currently uses Python2.

This project was originally created to extract JPG's out of the Android Thumbdata3 format.

It is theoretically capable of extracting data from any file that contains multiple JPG's within.

## Usage

Usage is quite simple. In the following example, the filename is simply `thumbdata3`:

```bash
./extract.py --file thumbdata3
```

The script will then output all JPG's to the same directory. These are the files you are after, named sequentially.
