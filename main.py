import io
import os
from time import perf_counter
from multiprocessing import Pool

import img2pdf
import pdf2image
from PIL import ImageEnhance, Image
from tqdm import tqdm

contrast: float = 1.6
brightness: float = 0.75


def process(file_name: str) -> None:
    """
    Adjusts both brightness and contrast
    'input' is prepended to filename for ingesting files
    'output' is prepended to filename for writing files
    """

    input_path: str = os.path.join("input", file_name)  # input file name 🤓
    output_path: str = os.path.join("output", file_name)  # output file name 🤓
    output_images: list[bytes] = []  # used for constructing output pdf

    for raw_img in tqdm(pdf2image.convert_from_path(input_path), desc=f"{file_name}", unit="page"):
        im_1: Image = ImageEnhance.Brightness(raw_img).enhance(brightness)
        out_im: Image = ImageEnhance.Contrast(im_1).enhance(contrast)
        out_img_bytes: io.BytesIO = io.BytesIO()

        out_im.save(out_img_bytes, format="JPEG")
        output_images.append(out_img_bytes.getvalue())

    with open(output_path, "wb") as outf:
        img2pdf.convert(*output_images, outputstream=outf)


if __name__ == "__main__":
    if not os.path.exists("input/"):
        raise Exception("Please place input files in 'input/'")
    if not os.path.exists("output/"):
        os.mkdir("output")

    start_time: float = perf_counter()  # for timing execution
    with Pool(processes=4) as pool:
        pool.map(process, os.listdir("input"))
    print(f"completed in: {perf_counter() - start_time}")  # for timing execution
