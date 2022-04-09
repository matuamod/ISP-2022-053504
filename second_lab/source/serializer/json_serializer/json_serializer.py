from source.serializer.base_serializer.base_serializer import BaseSerializer

class JSON_Serializer(BaseSerializer):
    
    _str = ""

    def __init__(self):
        super().__init__()

    def dump(self, obj : any, file_path : str):
        pass

    def dumps(self, obj : any) -> str:
        self._str = ""
        self._inspect(obj)
        return self._str

    def load(self, file_path : str) -> any:
        pass

    def loads(self, file_path : str) -> any:
        pass

    def _add(self, type_str : str):
        self._str += type_str
        
    def _inspect(self, obj):
        primitive_types = (int, float, bool, str, tuple, list, bytes)
        if type(obj) in primitive_types:
            self._inspect_primitive_type(obj)

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
        elif prim_obj_type in (list, tuple):
            self._add('[')
            for i, part_obj in enumerate(prim_obj):
                if i != 0:
                    self._add(',')
                self._inspect(part_obj)
            self._add(']')
