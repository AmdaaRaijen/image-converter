from PIL import Image
import os

input_dir = 'input/'
output_dir = 'output/'

def main():
    files = os.listdir(input_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    for file in files:
        image = Image.open(input_dir + file)
        
        new_file = file.split('.')[0] + '.webp'

        image.save(output_dir + new_file, format='webp')
        print(f'{file} converted to webp format')

if __name__ == '__main__':
    main()