from collections import OrderedDict
from io import TextIOWrapper
from typing import Any, Dict, Iterator, List, Optional, Union

from django.core.serializers.base import DeserializedObject
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey, ManyToManyField

from django.core.serializers import base
from django.db.models.fields import Field

class Serializer(base.Serializer):
    options: Dict[Any, Any]
    selected_fields: None
    stream: TextIOWrapper
    use_natural_foreign_keys: bool
    use_natural_primary_keys: bool
    internal_use_only: bool = ...
    objects: List[Any] = ...
    def start_serialization(self) -> None: ...
    def end_serialization(self) -> None: ...
    def start_object(self, obj: Model) -> None: ...
    def end_object(self, obj: Model) -> None: ...
    def get_dump_object(self, obj: Model) -> OrderedDict: ...
    def handle_field(self, obj: Model, field: Field) -> None: ...
    def handle_fk_field(self, obj: Model, field: ForeignKey) -> None: ...
    def handle_m2m_field(self, obj: Model, field: ManyToManyField) -> None: ...
    def getvalue(self) -> List[OrderedDict]: ...

def Deserializer(
    object_list: Union[
        List[Dict[str, Optional[Union[Dict[str, Optional[str]], str]]]],
        List[Dict[str, Union[Dict[str, Union[List[int], int, str]], int, str]]],
        List[OrderedDict],
    ],
    *,
    using: Any = ...,
    ignorenonexistent: bool = ...,
    **options: Any
) -> Iterator[DeserializedObject]: ...
