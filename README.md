# image-binder
This script merges multiple images into one image. For example 2x1 box or 4x4 etc...



### Usage:
###### Help:
To get help just type:

  `python bind.py -h`

Commands:
```

python bind.py bind.py -h

     _                                  _     _           _
    (_)_ __ ___   __ _  __ _  ___      | |__ (_)_ __   __| | ___ _ __
    | | '_ ` _ \ / _` |/ _` |/ _ \_____| '_ \| | '_ \ / _` |/ _ \ '__|
    | | | | | | | (_| | (_| |  __/_____| |_) | | | | | (_| |  __/ |
    |_|_| |_| |_|\__,_|\__, |\___|     |_.__/|_|_| |_|\__,_|\___|_|
                       |___/
                   
usage: python binder.py [-h] -sx N -sy M -i [img1, img2...] -o output_img.tiff
                    [-opt True]

optional arguments:
  -h, --help            show this help message and exit
  -sx N, --sizex N      Horizontal images number
  -sy M, --sizey M      Vertical images number
  -i [img1, img2...], --input [img1, img2...]
                        Input images to be binded
  -o output_img.tiff, --output output_img.tiff
                        Output image
  -opt, --optimize      Saved file optimization

Bye!

```

`-sx` and `-sy` specifies the size of output 'image box'. For example `-sx 2 -sy 2` means that your output image will contain 4 images and have size of 2 images vertically and 2 images horizontally.

`-opt` or `-optimize` enables `optimize` flag in PIL, so the size of ouput image will be reduced. 

I wanted to make it 100% 10/10 rated in pylint :).


Feel free to contribute. 


### TODO:
- [x] Argparse argument parsing
- [ ] filling blank places (for example 3 image box) with predefined color
- [ ] specifing size of output image in px
- [ ] TBD
