# Image-Capture-Device-Encoding

### Task Background Information

Imagine you are working with a low-level interface to an image capture device (e.g. a digital
camera or bar code scanner) that emits only monochrome data for fast signal processing. This
means that the pixel data that the device emits consists only of black and white information
that can be represented with a simple one (black) or zero (white).

The device represents images using column-oriented ‘pixel streams’, where a column is a
vertical sequence of pixel data. Due to hardware limitations in the device, it is capable of
managing only 4 pixel streams at once, so a given output pixel stream is comprised of the
concatenated sequence of every fourth column of pixel data:

In the example image above, the 8x8 image is exposed by the device as 4 pixel streams, where
stream S0 has columns {0,4}, stream S1 has columns {1,5}, stream S2 has columns {2,6}, and
stream S3 has columns {3,7}.

Using this scheme, the device can capture images of an arbitrary height but they must have a
configured, fixed with. For this exercise, assume the device is configured to capture images
exactly 100 pixels wide. This means that each of the 4 pixel streams for a given image is made
up of the sequence of pixels for 25 columns.

Assume that the device is dumping image data into a separate file per image capture, and your
job is to parse a given image file to allow additional processing. The file is a basic ASCII-encoded sequence of lines, where each line contains information about a single column stream
terminated with a single newline character (UNIX line format). (It should be noted that the Unix
newline is different than the Windows newline format and opening a file up in Windows
notepad will not read properly.) :

```
...
2 11 0 #S2, eleven 0’s
0 7 1 #S0, seven 1’s
2 4 1 #S2, four 1’s
...
```

Note that the device employs a basic run-length encoding scheme to represent the sequence of
pixel data for a given pixel stream. In the example above, the first line indicates that at this
point in the stream column stream index 2 has a sequence of 11 zeroes in a row, and stream
index 0 has seven ones in a row, and then stream index 2 has an additional four ones.

### Task Part 1 – Load a File

You have been provided with a file: ‘stream-data.dat’ that contains the output of the
device in the format as described above. Your first task is to load this file, parsing each stream
in its entirety. You should output from this part some basic information about each stream in
the following format:

```
Stream #0: <###> total pixels, <###> ones, <###> zeroes
Stream #1: <###> total pixels, <###> ones, <###> zeroes
Stream #2: <###> total pixels, <###> ones, <###> zeroes
Stream #3: <###> total pixels, <###> ones, <###> zeroes

Image Height: <###> pixels
```

In the required output, you should emit the total pixel count as well as the number of ones and
zeroes for each stream. You can then use this information to calculate the total image height
(assuming a width of 100 pixels as noted above) and emit this as well.

### Task Part 2 – Emit an Image

Once you have loaded the file, you should output it into a format that can be opened/visualized
in a more generic way than this odd per-stream format from the device. For the purpose of this
exercise, you can use the portable bitmap format (PBM) which provides a very simple, ASCIIbased
approach that can be opened in many image editing programs. In a basic PBM file, each
pixel is represented by an ASCII 1 or 0, with each line representing a row of pixel data. The
following is an example PBM for the 8x8 image drawn earlier:

```
P1
8 8
00000000
00100100
00100100
00000000
00000000
01000010
00111100
00000000
```

Note the three major parts:

1. A header line with the text “P1” indicating the type of image (1 being most basic, version 1 of the format)


2. A line indicating the dimensions of the image: WIDTH HEIGHT
3. A sequence of lines, one for each row of pixel data, where each pixel is an ASCII “0” or “1”.

For this part’s output we expect to see an 100xM image (where M is the height you calculate in
part (1)).

*Note:*
*This format is clearly very basic and not particularly efficient. In addition, the PBM format*
*technically limits pixels-per-row to 70 (forcing overflow onto the next line), but we will accept a*
*submission with 100 pixels per row as well.*

### Task Part 3 – Re-encode for More Efficiency

With the image decoded and available in-memory in your program, you can now consider how
to represent the image using fewer total bits than the device did. Develop and use whatever
encoding/compression scheme you’d like to take the raw pixel data, encode it, and then redecode
it to show that your scheme fully recreates the original image.

The scheme you use is up to you. We will be looking for the following in your submission:

1. A clear statement of how you are going to encode the image data (you can do so in the comments in your code)


2. An output file containing the result of your encoding. It should be smaller than the file we provided.


3. The results of decoding your encoded image. It should match the submission from part (2)