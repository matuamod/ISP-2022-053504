from dataclasses import dataclass

@dataclass
class DTO():
    dto_type = "dto_type"
    name = "name"
    code = "code"
    fields = "fields"
    global_types = "globals"

@dataclass
class DTO_TYPE():
    obj_type = "obj"
    func = "func"
    code = "code"
    model = "model"
    list = "list"
    dict = "dict"
    class_type_atrr = "class"
    nlocals_atrr = "co_nlocals"
    argcount_atrr = "co_argcount"
    varnames_atrr = "co_varnames"
    names_atrr = "co_names"
    cellvars_atrr = "co_cellvars"
    freevars_atrr = "co_freevars"
    posonlyagrcount_atrr = "co_posonlyagrcount"
    kwonlyargcount_atrr = "co_kwonlyargcount"
    firstlineno_atrr = "co_firstlineno"
    lnotab_atrr = "co_lnotab"
    stacksize_atrr = "co_stacksize"
    code_attr_atrr = "co_code"
    consts_atrr = "co_consts"
    flags_atrr = "co_flags"