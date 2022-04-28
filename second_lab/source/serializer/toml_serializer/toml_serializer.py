from types import NoneType, WrapperDescriptorType, MethodDescriptorType, BuiltinFunctionType, MappingProxyType, GetSetDescriptorType, ModuleType
from source.parser.toml_parser.toml_parser import TOML_Parser
from source.serializer.base_serializer.base_serializer import BaseSerializer
from source.dto.dto import DTO, DTO_TYPE
import inspect


class TOML_Serializer(BaseSerializer):

    _str = ""
    _toml_parser = None


    def __init__(self):
        super().__init__()
        self._toml_parser = TOML_Parser()

    
    def dump(self, obj: any, file_path: str):
        pass


    def dumps(self, obj: any):
        pass


    def load(self, file_path: str):
        pass


    def loads(self, s: str) -> any:
        pass


    def _inspect(self, obj: any):
        primitive_types = (int, float, bool, str, bytes)
        