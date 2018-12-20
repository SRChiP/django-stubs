from io import BufferedReader, BytesIO
from typing import Any, Union

from django.core.files import File

class ImageFile(File):
    file: BufferedReader
    mode: str
    name: str
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...

def get_image_dimensions(file_or_path: Union[BufferedReader, BytesIO, ImageFile, str], close: bool = ...) -> Any: ...
