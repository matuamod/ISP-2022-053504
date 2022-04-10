from dataclasses import dataclass

@dataclass
class DTO():
    dto_type = "dto_type"
    code = "code"
    name = "name"
    field = "field"
    path = "path"
    globals = "globals"


@dataclass
class DTO_TYPE():
    obj_type = "obj"
    func = "func"
    code = "code"
    model = "model"
    list = "list"
    dict = "dict"
    class_type = "class"