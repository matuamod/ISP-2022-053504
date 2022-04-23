import re
from source.dto.dto import DTO_TYPE, DTO
from source.parser.parse_arguments import parse_arguments


class JSON_Parser():

    _arg_dict = parse_arguments


    def _get_arg_dict(self) -> dict:
        return self._arg_dict


    def _change_arg_list(self, arg_type: tuple, arg_list: list, get_value: bool = False) -> list:
        if len(arg_list) > 0:
            if arg_type in arg_list:
                arg_list.pop(0)
            return(arg_list if get_value == False else (arg_list, arg_type))


    def _get_parse_arg(self, json_str: str) -> list:
        json_str = json_str.replace(" ", "")
        arg_dict = self._get_arg_dict()
        arguments = []

        while len(json_str) > 0:

            for argument in arg_dict.parse_arg.items():
                try:
                    expr = re.match(argument[1], json_str)
                    if expr.start() == 0:
                        json_str = json_str[0: expr.start():] + \
                            json_str[expr.end()::]
                        # print("Deleted argument is : " + str(expr.group()))
                        if argument[0] == arg_dict.number:
                            number = float(expr.group()) if "." in expr.group() else int(
                                expr.group())
                            arguments.append((argument[0], number))
                        elif argument[0] == arg_dict.bool_arg:
                            boolean = True if expr.group() == "true" else False
                            arguments.append((argument[0], boolean))
                        elif argument[0] == arg_dict.str_arg:
                            arguments.append(
                                (argument[0], expr.group().replace('"', '')))
                        elif argument[0] == arg_dict.none:
                            arguments.append((argument[0], None))
                        else:
                            arguments.append((argument[0],))
                except:
                    None
        return arguments


    def _get_first_arg(self, arg_list: dict) -> any:
        return (arg_list[0] if len(arg_list) > 0 else None)


    def _parse_prim_types(self, arg_list: list) -> any:
        res_prim = None
        arg_dict = self._get_arg_dict()
        parse_prim = self._get_first_arg(arg_list)
        prim_parse_tuple = (arg_dict.number, arg_dict.str_arg,
                            arg_dict.bool_arg, arg_dict.none)
        if parse_prim[0] in prim_parse_tuple:
            result = parse_prim[1]
            if parse_prim[0] in arg_dict.str_arg:
                if result.isdigit():
                    result = bytes.fromhex(result)
            arg_list = self._change_arg_list(parse_prim, arg_list)
            return result


    def _parse_list_tuple(self, arg_list: list) -> list:
        res_list = []
        arg_dict = self._get_arg_dict()
        parse_list_item = self._get_first_arg(arg_list)
        if parse_list_item[0] in arg_dict.right_bracket:
            arg_list = self._change_arg_list(parse_list_item, arg_list)

            while self._get_first_arg(arg_list)[0] != arg_dict.left_bracket:
                if self._get_first_arg(arg_list)[0] == arg_dict.comma:
                    arg_list = self._change_arg_list(
                        self._get_first_arg(arg_list), arg_list)
                res_list.append(self._make_parse(arg_list))

            arg_list = self._change_arg_list(parse_list_item, arg_list)
        return res_list


    def _get_dto_name(self, arg_list: list) -> str:
        dto_names = ('dict', 'func', 'class',
                     'code', 'module', 'obj')

        for count in range(4):
            argument = self._get_first_arg(arg_list)
            if argument[0] == 'str' and argument[1] in dto_names:
                dto_name = argument[1]
            arg_list = self._change_arg_list(argument, arg_list)
        argument = self._get_first_arg(arg_list)
        return (arg_list, dto_name)


    def _parse_dto(self, arg_list: list) -> any:
        arg_list = self._change_arg_list(
            self._get_first_arg(arg_list), arg_list)
        arg_list, dto_type = self._get_dto_name(arg_list)
        if dto_type == DTO_TYPE.dict:
            arg_list, result = self._parse_dict(arg_list)
        if dto_type == DTO_TYPE.func:
            arg_list, result = self._parse_func(arg_list)
        return result


    def _parse_dict(self, arg_list: list) -> dict:
        res_dict = {}

        while self._get_first_arg(arg_list)[0] != self._arg_dict.left_brace:
            if len(self._get_first_arg(arg_list)) == 2:
                arg_list, dict_key = self._change_arg_list(
                    self._get_first_arg(arg_list), arg_list, get_value=True)
                arg_list = self._change_arg_list(
                    self._get_first_arg(arg_list), arg_list)
                arg_list, dict_value = self._change_arg_list(
                    self._get_first_arg(arg_list), arg_list, get_value=True)
                if self._get_first_arg(arg_list)[0] == self._arg_dict.comma:
                    arg_list = self._change_arg_list(
                        self._get_first_arg(arg_list), arg_list)
            key = self._make_parse([dict_key])
            value = self._make_parse([dict_value])
            res_dict[key] = value
        arg_list = self._change_arg_list(
            self._get_first_arg(arg_list), arg_list)
        return (arg_list, res_dict)


    def _parse_func(self, arg_list: list) -> any:
        print("Hello world")
        result = 0
        return (arg_list, result)


    def _make_parse(self, arg_list: list) -> any:
        argument = self._get_first_arg(arg_list)
        if argument[0] == self._arg_dict.right_brace:
            result = self._parse_dto(arg_list)
        elif argument[0] == self._arg_dict.right_bracket:
            result = self._parse_list_tuple(arg_list)
        else:
            result = self._parse_prim_types(arg_list)
        return result


    def _parse(self, json_str: str) -> any:
        arg_list = self._get_parse_arg(json_str)
        return self._make_parse(arg_list)
