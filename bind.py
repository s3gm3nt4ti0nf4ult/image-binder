
'''
    Image-binder is a very simple tool designed to combine multiple images
    for example data charts or diagrams, side by side into single image
'''

__author__ = 's3gm3nt4ti0nf4ult'
__licence__ = 'MIT'

import sys
import argparse
from PIL import Image


def img_sizer(img_list):
    '''searches the biggest image'''
    x_s, y_s = 0, 0
    for i in img_list:
        try:
            image = Image.open(i)
            image_x_s, image_y_s = image.size
            if image_x_s > x_s:
                x_s = image_x_s
            if image_y_s > y_s:
                y_s = image_y_s
        except FileNotFoundError:
            print('Cannot open file {}, exiting!'.format(i))
            sys.exit(1)
    if x_s == 0 or y_s == 0:
        print('Size error, biggest image is 0x0 ppi!, exiting!')
        sys.exit(1)
    print("Largest image size {} px x {} px\n".format(x_s, y_s))

    return x_s, y_s



def resize(img_list, size_x, size_y):
    '''resizes to the biggest image size found by img_size()'''
    for i in img_list:
        try:
            img = Image.open(i)
            if img.size != (size_x, size_y):
                print("Resizing {}".format(i))
                img = img.resize((size_x, size_y), Image.ANTIALIAS)
                img.save(i)
            else:
                pass
        except (FileNotFoundError, IOError, ValueError) as error:
            print('Error while processing {} file occured. Exiting:\n{}'.format(i, error))



def make_image(box_x, box_y, ppi_x, ppi_y, images):
    '''does the core of binding'''

    image_s_x = box_x * ppi_x
    image_s_y = box_y * ppi_y

    print('{} x {}\n{} px x {} px'.format(ppi_x, ppi_x, image_s_x, image_s_y))

    pos_x, pos_y = 0, 0
    result = Image.new('RGB', (image_s_x, image_s_y))
    for i in images:
        print('Pasting {} in {} x {} '.format(i, pos_x, pos_y))
        try:
            img = Image.open(i)
            result.paste(img, (pos_x, pos_y, pos_x+ppi_x, pos_y+ppi_y))
        except (FileNotFoundError, IOError, ValueError) as error:
            print('Error while processing {} file occured. Exiting:\n{}'.format(i, error))
            sys.exit(1)
        if (images.index(i) + 1) % box_x == 0:
            pos_x = 0
            pos_y += ppi_y
        elif images.index(i) == 0 or images.index(i)+1 % box_x != 0:
            pos_x += ppi_x

    return result




def hello():
    '''Function displays hello prompt'''
    print(r'''
     _                                  _     _           _
    (_)_ __ ___   __ _  __ _  ___      | |__ (_)_ __   __| | ___ _ __
    | | '_ ` _ \ / _` |/ _` |/ _ \_____| '_ \| | '_ \ / _` |/ _ \ '__|
    | | | | | | | (_| | (_| |  __/_____| |_) | | | | | (_| |  __/ |
    |_|_| |_| |_|\__,_|\__, |\___|     |_.__/|_|_| |_|\__,_|\___|_|
                       |___/
                   ''')


def main(argv):
    '''main function'''


    parser = argparse.ArgumentParser(prog=argv[0], add_help=True,
                                     description=hello(), epilog='Bye!')
    parser.add_argument('-sx', '--sizex', metavar='N', required=True,
                        type=int, help='Horizontal images number')
    parser.add_argument('-sy', '--sizey', metavar='M', required=True,
                        type=int, help='Vertical images number')
    parser.add_argument('-i', '--input', metavar='img1, img2...',
                        required=True, type=str, nargs='+', help='Input images to be binded')
    parser.add_argument('-o', '--output', metavar='output_img.tiff',
                        required=True, type=str, help='Output image')
    parser.add_argument('-dopt', '--doptimize', required=False, action='store_true',
                        help='Disables saved file optimization')
    arguments = parser.parse_args()

    blok_size_x = arguments.sizex
    blok_size_y = arguments.sizey
    input_images = arguments.input
    output_name = arguments.output
    opt = arguments.doptimize

    if (output_name.split('.')[-1].lower() != 'tiff' and
            output_name.split('.')[-1].lower() != 'tif'):
        output_name += '.tif'

    max_ppi_x, max_ppi_y = img_sizer(input_images)
    output_image = make_image(blok_size_x, blok_size_y, max_ppi_x, max_ppi_y, input_images)


    print('Saving as {} with optimization set to: {}'.format(output_name, opt))
    output_image.save(output_name, optimize=opt)



if __name__ == '__main__':
    main(sys.argv)
