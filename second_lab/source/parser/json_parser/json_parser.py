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


    def _parse_dto(self, dto_str: str) -> list:
        dto_list = []

        if dto_str[0] == '{':
            dto_str = dto_str[1 : -1]
            dto_str = dto_str.replace(' ', '')
        dto_list = re.split(',', dto_str)
        if "dict" in dto_list[0]:
            dto = self._parse_dict(dto_str)
        elif "func" in dto_list[0]:
            self._parse_func(dto_str)
            dto = 0
        return dto


    def _parse_dict(self, dict_str: str) -> dict:
        dict_list = re.split(',', dict_str)
        dict_list.pop(0)
        dict_elem_list = []
        i = 0
        res_dict = {}
        
        for elem in dict_list:
            dict_elem_list.append(re.split(':', elem))

            for j in range(2):
                if j == 0:
                    key = self._make_parse(dict_elem_list[i][j])
                elif j == 1:
                    value = self._make_parse(dict_elem_list[i][j])
                    res_dict[key] = value
            i += 1
        return res_dict


    def _parse_func(self, func_str: str):
        print(func_str)
        


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