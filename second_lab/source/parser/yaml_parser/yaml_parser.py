from source.dto.dto import DTO, DTO_TYPE
import yaml

class YAML_Parser():

    def _make_parse(self, yaml_str: str) -> any:
        
        res_obj = yaml.full_load(yaml_str)
        return res_obj