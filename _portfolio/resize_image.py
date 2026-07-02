# resize_image.py
import argparse
from pathlib import Path

from PIL import Image, ImageOps


def main(args) -> None:

    with Image.open(args.input) as image:
        # image = ImageOps.fit(
        #     image.convert("RGB"),
        #     (500, 300),
        #     method=Image.Resampling.LANCZOS,
        # )
        resized = image.resize((500, 300), Image.Resampling.LANCZOS)
        resized.save(args.output, quality=95)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", default="/pareto_splat.png", type=Path)
    parser.add_argument("output", default="/pareto_splat_resized.png", type=Path)
    args = parser.parse_args()
    main(args)
    
    # python image_resize.py pareto_splat.png pareto_splat_resized.png
