from types import NoneType
from source.parser.json_parser.json_parser import JSON_Parser
from source.serializer.base_serializer.base_serializer import BaseSerializer
from source.dto.dto import DTO, DTO_TYPE
import inspect


class JSON_Serializer(BaseSerializer):

    _str = ""
    _json_parser = None
 

    def __init__(self):
        super().__init__()
        self._json_parser = JSON_Parser()


    def dump(self, obj: any, file_path: str):
        file = open(file_path, "w")
        _str = self.dumps(obj)
        file.write(_str)
        file.close()


    def dumps(self, obj: any) -> str:
        self._str = ""
        self._inspect(obj)
        return self._str


    def load(self, file_path: str) -> any:
        obj = None
        file = open(file_path, "r")
        _str = file.read()
        obj = self.loads(_str)
        return obj


    def loads(self, s: str) -> any:
        return self._json_parser._parse(s)


    def _add(self, type_str: str):
        self._str += type_str


    def _inspect(self, obj):
        primitive_types = (int, float, bool, str, bytes)
        if type(obj) in primitive_types:
            self._inspect_primitive_type(obj)
        elif type(obj) in (tuple, list):
            self._inspect_list_tuple_type(obj)
        elif obj == None:
            self._add("null")
        else:
            self._add("{")
            if type(obj) == dict:
                self._inspect_dict_type(obj)
            elif inspect.isfunction(obj):
                self._inspect_func_type(obj)
            self._add("}")


    def _inspect_primitive_type(self, prim_obj):
        prim_obj_type = type(prim_obj)
        if prim_obj_type in (int, float):
            self._add(f'{prim_obj}')
        elif prim_obj_type == bool:
            if prim_obj:
                bool_value = "true"
            else:
                bool_value = "false"
            self._add(f'{bool_value}')
        elif prim_obj_type == str:
            self._add(f'"{prim_obj}"')
        elif prim_obj_type == bytes:
            hexademical = prim_obj.hex()
            self._add(f'"{hexademical}"')


    def _inspect_list_tuple_type(self, obj):
        if(len(obj)) == 0:
            self._add('[]')
        else:
            self._add('[')
            for i, part_obj in enumerate(obj):
                if i != 0:
                    self._add(',')
                self._inspect(part_obj)
            self._add(']')


    def _inspect_dict_type(self, dict_obj: dict):
        self._add(f'"{DTO.dto_type}": "{DTO_TYPE.dict}"')
        if len(dict_obj) >= 1:
            self._add(",")
            is_first_el = True
            i = 0

        for key, value in dict_obj.items():
            if is_first_el != True:
                self._add(',')
            self._inspect(key)
            self._add(': ')
            self._inspect(value)
            is_first_el = False


    def _inspect_func_type(self, func_obj):
        self._add(f'"{DTO.dto_type}": "{DTO_TYPE.func}",')
        self._add(f'"{DTO.name}": "{func_obj.__name__}",')
        self._add(f'"{DTO.global_types}": ')
        curr_globals_dict = self._get_globals(func_obj)
        self._inspect(curr_globals_dict)
        self._add(',')
        self._get_code(func_obj)
        self._add(',')
        self._add(f'"{DTO.closure}": "{func_obj.__closure__}"')


    def _get_globals(self, func_obj) -> dict:
        globals_type = func_obj.__globals__
        curr_globals_dict = dict()
        code_obj = func_obj.__code__

        for key, value in globals_type.items():
            if key in code_obj.co_names:
                curr_globals_dict.update({key: value})
        return curr_globals_dict


    def _get_code(self, func_obj):
        code_obj = func_obj.__code__
        self._add(f'"{DTO.code}": ')
        self._add('{')
        self._add(f'"{DTO.dto_type}": "{DTO_TYPE.code}",')
        self._add(f'"{DTO.fields}": ')
        curr_code_dict = self._get_code_fields(code_obj)
        self._inspect(curr_code_dict)
        self._add('}')


    def _get_code_fields(self, code_obj) -> dict:
        curr_code_dict = dict()
        variables = (
            "co_nlocals", "co_argcount",
            "co_varnames", "co_names",
            "co_cellvars", "co_freevars",
            "co_posonlyagrcount", "co_kwonlyargcount",
            "co_firstlineno", "co_lnotab",
            "co_stacksize", "co_code", "co_name",
            "co_consts", "co_flags", "co_filename"
        )

        for member in inspect.getmembers(code_obj):
            if member[0] in variables:
                curr_code_dict.update({member[0]: member[1]})
        return curr_code_dict
