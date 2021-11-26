# Python Image Extractor

This project currently uses Python3.

This project was originally created to extract JPG's out of the Android Thumbdata3 format.

It is theoretically capable of extracting data from any file that contains multiple JPG's within.

## Usage

Usage is quite simple. In the following example, the filename is simply `thumbdata3`:

```bash
./extract.py --file thumbdata3
```

The script will then output all JPG's to the same directory. These are the files you are after, named sequentially.

The0tter fork:
Updated to Python3
All errors in update are mine.

Note:  If some of the JPGs are recursive, the extractor will recursively split the files, possibly creating a few 
invalid, small files.  For example I had a thumb drive image that had 40 JPG files if I mounted it as an image, but when 
running it through the extractor I ended up with 57 extracted files, because one of the 40 had another 15 JPGs in it, and 
it created 2 invalid files.  What I was after was actually in one of the 15, so the fact that it just plowed in was a
benefit, but it is a feature that may surprise in some instances.

The file can be modified to any file type for extraction by modifying the start of image and end of image flags to match,
so if you want to extract .PNG files you could look up the magic numbers for PNG and modify the strings.  
