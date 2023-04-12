import argparse
import glob
import os
from PIL import Image
from tqdm import tqdm


def main(args):
    # For DF2K, we consider the following three scales,
    # and the smallest image whose shortest edge is 400
    scale = args.scale # 0.25
   # shortest_edge = 400

    path_list = sorted(glob.glob(os.path.join(args.input, '*')))
    for path in tqdm(path_list):
       # print(path)
        basename = os.path.splitext(os.path.basename(path))[0]

        img = Image.open(path)
        width, height = img.size
        # for scale in enumerate(scale_list):
      #  print(f'\t{scale:.2f}')
        if args.method == 'bicubic':
          rlt = img.resize((int(width * scale), int(height * scale)), resample=Image.BICUBIC)
        else:
          rlt = img.resize((int(width * scale), int(height * scale)), resample=Image.LANCZOS) 
        rlt.save(os.path.join(args.output, f'{basename}.png'))

        # save the smallest image which the shortest edge is 400
        # if width < height:
        #     ratio = height / width
        #     width = shortest_edge
        #     height = int(width * ratio)
        # else:
        #     ratio = width / height
        #     height = shortest_edge
        #     width = int(height * ratio)
        # rlt = img.resize((int(width), int(height)), resample=Image.LANCZOS)
        # rlt.save(os.path.join(args.output, f'{basename}T{idx+1}.jpeg'))


if __name__ == '__main__':
    """Generate multi-scale versions for GT images with LANCZOS resampling.
    It is now used for DF2K dataset (DIV2K + Flickr 2K)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='datasets/RLKA-NET/data/FLIR/train_gt', help='Input folder')
    parser.add_argument('--output', type=str, default='datasets/RLKA-NET/data/FLIR/train_lrx2', help='Output folder')
    parser.add_argument('--scale', default = 0.5, help='scale for bicubic')
    parser.add_argument('--method', default = 'bicubic',type='str', help=' downsample method ' )
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    main(args)
    print('Done!')
