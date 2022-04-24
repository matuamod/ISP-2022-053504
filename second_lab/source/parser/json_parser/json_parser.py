import re
from source.dto.dto import DTO_TYPE, DTO
from source.parser.parse_arguments import parse_arguments
from types import CodeType, FunctionType, ModuleType


class JSON_Parser():

    _arg_dict = parse_arguments


    def _get_arg_dict(self) -> dict:
        return self._arg_dict


    def _change_arg_list(self, arg_type: tuple, arg_list: list, get_value: bool = False) -> list:
        if len(arg_list) > 0:
            if arg_type in arg_list:
                arg_list.pop(0)
            return(arg_list if get_value == False else (arg_list, arg_type))


    def _change_arg_list_fast(self, arg_type: tuple, arg_list: list, count: int) -> list:
        for i in range(count):
            arg_list = self._change_arg_list(
                self._get_first_arg(arg_list), arg_list)
        return arg_list


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

            arg_list = self._change_arg_list(
                self._get_first_arg(arg_list), arg_list)
        return (arg_list, res_list)


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
        elif dto_type == DTO_TYPE.func:
            arg_list, result = self._parse_func(arg_list)
        return (arg_list, result)


    def _parse_dict(self, arg_list: list) -> dict:
        res_dict = {}
        # print(arg_list)

        while self._get_first_arg(arg_list)[0] != self._arg_dict.left_brace:
            if len(self._get_first_arg(arg_list)) == 2:
                arg_list, dict_key = self._change_arg_list(
                    self._get_first_arg(arg_list), arg_list, get_value=True)
                key = self._make_parse([dict_key])
                arg_list = self._change_arg_list(
                    self._get_first_arg(arg_list), arg_list)
                if self._get_first_arg(arg_list)[0] != self._arg_dict.right_bracket:
                    arg_list, dict_value = self._change_arg_list(
                        self._get_first_arg(arg_list), arg_list, get_value=True)
                    value = self._make_parse([dict_value])
                else:
                    arg_list, value = self._make_parse(arg_list)
                    # print(arg_list)
                if self._get_first_arg(arg_list)[0] == self._arg_dict.comma:
                    arg_list = self._change_arg_list(
                        self._get_first_arg(arg_list), arg_list)
            res_dict[key] = value
        while self._get_first_arg(arg_list)[0] == self._arg_dict.left_brace:
            arg_list = self._change_arg_list(
                self._get_first_arg(arg_list), arg_list)
        return (arg_list, res_dict)


    def _parse_func_name(self, arg_list: list) -> str:
        arg_list = self._change_arg_list_fast(
            self._get_first_arg(arg_list), arg_list, 2)
        arg_list, tuple_name = self._change_arg_list(
            self._get_first_arg(arg_list), arg_list, get_value=True)
        arg_list = self._change_arg_list_fast(
            self._get_first_arg(arg_list), arg_list, 1)
        func_name = self._make_parse([tuple_name])
        return (arg_list, func_name)


    def _parse_func_globals(self, arg_list: list) -> dict:
        arg_list = self._change_arg_list_fast(
            self._get_first_arg(arg_list), arg_list, 2)
        arg_list, res_dict = self._make_parse(arg_list)
        return (arg_list, res_dict)


    def _parse_func_code(self, arg_list: list) -> CodeType:
        arg_list = self._change_arg_list_fast(
            self._get_first_arg(arg_list), arg_list, 10)
        arg_list, code_dict = self._make_parse(arg_list)
        print(code_dict)

        res_code = CodeType(
            code_dict["co_argcount"], code_dict["co_posonlyargcount"],
            code_dict["co_kwonlyargcount"], code_dict["co_nlocals"],
            code_dict["co_stacksize"], code_dict["co_flags"],
            bytes.fromhex(code_dict["co_code"]), tuple(code_dict["co_consts"]),
            tuple(code_dict["co_names"]), tuple(code_dict["co_varnames"]),
            code_dict["co_filename"], code_dict["co_name"],
            code_dict["co_firstlineno"], code_dict["co_lnotab"],
            tuple(code_dict["co_freevars"]), tuple(code_dict["co_cellvars"]),
        )
        return (arg_list, res_code)


    def _parse_func(self, arg_list: list) -> any:
        argument = self._get_first_arg(arg_list)
        if argument[1] == DTO.name:
            arg_list, func_name = self._parse_func_name(arg_list)
            arg_list, func_globals = self._parse_func_globals(arg_list)
            arg_list, func_code = self._parse_func_code(arg_list)
            arg_list = self._change_arg_list_fast(
                self._get_first_arg(arg_list), arg_list, 3)
            arg_list, buf_closure = self._change_arg_list(
                self._get_first_arg(arg_list), arg_list, get_value=True)
            arg_list = self._change_arg_list_fast(
                self._get_first_arg(arg_list), arg_list, 1)
            func_closure = self._make_parse(buf_closure)
        res_func = FunctionType(func_code, func_globals,
                                func_name, func_closure)
        res_func.__globals__["__builtins__"] = __import__("builtins")
        return (arg_list, res_func)


    def _make_parse(self, arg_list: list) -> any:
        argument = self._get_first_arg(arg_list)
        if argument[0] == self._arg_dict.right_brace:
            arg_list, result = self._parse_dto(arg_list)
        elif argument[0] == self._arg_dict.right_bracket:
            arg_list, result = self._parse_list_tuple(arg_list)
        else:
            result = self._parse_prim_types(arg_list)
        return ((arg_list, result) if argument[0] == self._arg_dict.right_brace or\
                        argument[0] == self._arg_dict.right_bracket else result)


    def _parse(self, json_str: str) -> any:
        arg_list = self._get_parse_arg(json_str)
        arg_list, result = self._make_parse(arg_list)
        return result
