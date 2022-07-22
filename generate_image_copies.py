def generate_image_copies(path, img_title, limit):
  pic = None
  with open(f'{img_title}.png','rb') as r:
    pic = r.read()

  for n in range(1,limit):
    with open(f'{img_title}{n}.png','wb') as w:
        w.write(pic)
        
 if __name__ == '__main__':
  path = input('enter the directory you want to save the image files to')
  image_title = input('enter the filename of the image you want to duplicate')
  limit = input('enter the number of copies you want to generate')
  print('generating image copies')
  generate_image_copies(path, img_title, limit)
  print('done generating :)')
