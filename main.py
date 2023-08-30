"""
## USAGE
```
$ python pdf_contrast.py 2.3 -i in.pdf -o out.pdf
Loading pdf in.pdf
Pages: 48
Contrast x2.3: 100%|███████████████████████| 48/48 [00:02<00:00, 18.42pages/s]
Saving pdf to out.pdf
```
"""
import io
from PIL import ImageEnhance
import img2pdf
import pdf2image
from tqdm import tqdm

contrast: float = 1.6
brightness: float = 0.75


def pdf_contrast(input_file: str, output_file: str):
    """
    Create a new pdf corresponding to the contrast multiplier
    `input_file`: name the of the input_file
    `contrast`: contrast multiplier. 1 corresponds to no change
    `output_file`: name of the file to be saved
    """

    # print(f'Loading pdf {input_file}')
    input_images = pdf2image.convert_from_path(input_file)
    # print(f'Pages: {len(input_images)}')

    output_images: list[bytes] = []
    for raw_img in tqdm(input_images,
                    desc=f"Contrast x{contrast}",
                    unit="pages"
                    ):
        im_1 = ImageEnhance.Brightness(raw_img).enhance(brightness)
        out_im = ImageEnhance.Contrast(im_1).enhance(contrast)

        out_img_bytes = io.BytesIO()
        out_im.save(out_img_bytes, format="JPEG")
        output_images.append(out_img_bytes.getvalue())

    # print(f'Saving pdf to {output_file}')
    with open(output_file, "wb") as outf:
        img2pdf.convert(*output_images, outputstream=outf)


if __name__ == "__main__":
    pdf_contrast("0.pdf", "0-1.pdf")