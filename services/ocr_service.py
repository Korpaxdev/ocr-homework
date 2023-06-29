import os

from easyocr import Reader

from utils.modes_utils import GPU


def ocr_read_image(image: bytes, mode: str, languages):
    reader = Reader(languages, gpu=is_gpu(mode))
    return reader.readtext(image, detail=0, workers=get_cpu_count(), )


def is_gpu(mode, ):
    return mode == GPU


def get_cpu_count():
    return os.cpu_count()
