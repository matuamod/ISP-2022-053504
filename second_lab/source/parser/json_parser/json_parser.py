from jsonschema import ValidationError
from sympy import false
from source.dto.dto import DTO, DTO_TYPE
from source.parser.parse_arguments.parse_arguments import parse_arg
import re

class JSON_Parser():

    def _make_parse(self, parse_str: str):
        if parse_str[0] == '[':
            res = self._parse_list(parse_str)
        elif parse_str[0] == '{':
            res = self._parse_dto(parse_str)
        else:
            res = self._parse_prim_types(parse_str)
        return res


    def _parse_prim_types(self, prim_str: str) -> any:
        if self._is_bool(prim_str):
            return (True if prim_str == 'true' else False)
        elif self._is_text_or_byte(prim_str):
            prim_str = prim_str.replace('"', '')
            return (prim_str if not prim_str.isdigit() else bytes.fromhex(prim_str))
        elif self._is_number(prim_str):
            return (int(prim_str) if prim_str.isdigit() else float(prim_str))
            

    def _parse_list(self, list_str: str) -> list:
        buf_list = []
        res_list = []

        if '[' in list_str:
            list_str = re.sub('[^A-Za-z0-9," -]', "", list_str)
        buf_list = re.split(',', list_str)

        for item in buf_list:
            res_item = self._make_parse(item)
            res_list.append(res_item)
            if res_item == '':
                res_list.remove(res_item)
        return res_list


    def _parse_dto(self, dict_str: str) -> dict:
        pass
        

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
            if (chars[0] == '"' and chars[len(text) - 1] == '"'):
                return True
        except ValidationError:
            return False