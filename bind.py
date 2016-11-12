from PIL import Image
import sys

def check_box_size(l):
  if len(l) == 1:
    try:
      x = int(l)
      return x,1
    except:
      sys.exit("Size argument error\n")
  else:
    l = l.split('x')
    try:
      x = int(l[0])
      y = int(l[1])
      return x,y
    except:
      sys.exit("Size argument error\n")
  
  
def img_sizer(img_list):
  x_s, y_s = 0, 0
  for i in img_list:
    im = Image.open(i)
    x,y = im.size
    if x > x_s:
      x_s = x
    if y > y_s:
      y_s = y
  print("Largest image size {} px x {} px\n".format(x_s,y_s))
  return x_s,y_s
  
def resize(img_list,x,y):
  for i in img_list:
      try:
        img = Image.open(i)
        if img.size != (x,y):
          print("Resizing {}".format(i))
          img = img.resize((x,y), Image.ANTIALIAS)
          img.save(i)
        else:
          pass
      except:
        print('Error while processing {}'.format(i))

def make_image(box_x, box_y, x, y, images, name):
  if '.tif' != name[:-4]:
    name += '.tif'
  image_s_x = box_x * x
  image_s_y = box_y * y
  print('{} x {}\n{} px x {} px'.format(x, y, image_s_x, image_s_y))
  pos_x, pos_y = 0, 0
  result = Image.new('RGB', (image_s_x, image_s_y))
  for i in images:
    print('Pasting {} in {} x {} '.format(i, pos_x, pos_y))
    try:
      img = Image.open(i)
    except:
      print('Cannot open file {}.'.format(i))
    result.paste(img, (pos_x, pos_y, pos_x+x, pos_y+y))
    if (images.index(i) + 1) % box_x == 0:
      pos_x = 0
      pos_y += y
    elif images.index(i) == 0 or images.index(i)+1 % box_x != 0:
      pos_x += x
  result.save(name,optimize=True)
  
  
def handle(opt):
  name = input('Specify output file\n')
  b_x,b_y = check_box_size(opt[0])
  opt = opt[1:]
  if len(opt) != b_x * b_y:
    sys.exit('Invalid box size or number of arguments given')
  im_x, im_y = img_sizer(opt)
  resize(opt, im_x, im_y)
  make_image(b_x, b_y, im_x, im_y, opt, name)
  
  
def main(argv):
  if len(argv)<3:
    print("Usage:\npython {} box_size(xs)xbox_size_(ys) image1 image2 ...\n".format(argv[0]))
  else:
    handle(argv[1:])

    
if __name__ == '__main__':
  main(sys.argv)