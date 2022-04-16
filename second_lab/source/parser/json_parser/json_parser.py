from jsonschema import ValidationError
from sympy import false
from source.dto.dto import DTO, DTO_TYPE
from source.parser.parse_arguments.parse_arguments import parse_arg
import re

class JSON_Parser():

    def _make_list(self, json_str : str) -> list:
        if len(json_str) > 0:
            for item in parse_arg.items():
                if item[1] in json_str:
                    buff_str = re.match(item[1], json_str)
                    pass


    def _parse_prim_types(self, prim_str: str) -> any:
        if self._is_bool(prim_str):
            return (True if prim_str == 'true' else False)
        elif self._is_text_or_byte(prim_str):
            prim_str = prim_str.replace('"', '')
            return (prim_str if not prim_str.isdigit() else bytes.fromhex(prim_str))
        elif self._is_number(prim_str):
            return (int(prim_str) if prim_str.isdigit() else float(prim_str))
            

    def _parse_list(self, list_str: str) -> list:
        res_list = []

        if '[' in list_str:
            list_str = re.sub("[^A-Za-z0-9, -]", "", list_str)
        res_list = re.split(',', list_str)

        for item in res_list:
            if item == '':
                res_list.remove(item)
        return res_list
        

    def _is_number(self, numb_str: str) -> bool:
        try:
            if float(numb_str):
                return True
            elif int(numb_str):
                return True
        except ValidationError:
            return False


    def _is_bool(self, bool_str: str) -> bool:
        try:
            bool_tuple = ('true', 'false')
            if bool_str in bool_tuple:
                return True
        except ValidationError:
            return False
            

    def _is_text_or_byte(self, text: str) -> bool:
        try:
            chars = []

            for char in text:
                chars.append(char)
            if chars[0] == '"' and chars[len(text) - 1] == '"':
                return True
        except ValidationError:
            return False