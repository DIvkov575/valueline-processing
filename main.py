import io
import os
from time import perf_counter
from multiprocessing import Pool

import img2pdf
import pdf2image
from PIL import ImageEnhance, Image, ImageOps
from tqdm import tqdm

brightness: float = 1  # use this value to adjust brightness
lower_contrast_threshold = 25  # all pixels darker than lower_contrast_threshold will be snapped to 0 (black)


def process(file_name: str) -> None:
    """
    Adjusts both brightness and contrast
    'input' is prepended to filename for ingesting files
    'output' is prepended to filename for writing files
    """

    input_path: str = os.path.join("input", file_name)  # input file name 🤓
    output_path: str = os.path.join("output", file_name)  # output file name 🤓
    output_images: list[bytes] = []  # used for constructing output pdf

    im_1 = pdf2image.convert_from_path(input_path, dpi=75, grayscale=True)[0]
    # ImageOps.grayscale(im_1)  # greyscale image
    im_1: Image = ImageOps.autocontrast(im_1, (lower_contrast_threshold, 30))  # improve contrast by snapping pixels
    im_1: Image = ImageEnhance.Brightness(im_1).enhance(brightness)  # use to tweak brightness
    out_img_bytes: io.BytesIO = io.BytesIO()

    im_1.save(out_img_bytes, format="JPEG")
    output_images.append(out_img_bytes.getvalue())

    with open(output_path, "wb") as outf:
        img2pdf.convert(*output_images, outputstream=outf)

    print(file_name)


if __name__ == "__main__":
    # ensure input and output directory exists
    if not os.path.exists("input/"):
        raise Exception("Please place input files in 'input/'")
    if not os.path.exists("output/"):
        os.mkdir("output")

    # for file in os.listdir("input"):
    #     process(file)
    # process(os.listdir("input")[0])


    start_time: float = perf_counter()  # for timing execution
    with Pool(processes=4) as pool:
        pool.map(process, os.listdir("input"))
    print(f"completed in: {perf_counter() - start_time}")  # for timing execution
