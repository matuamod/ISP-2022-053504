# Matuamod serializer
#### My custom JSON, TOML, YAML serializer/parser

## Installation:
##### Write in your terminal:

```
pip install matuamod-serializer==0.2.1
pip install pyyaml
pip install toml
```

## Using as a library:
##### Simple example:

```
from matuamod_serializer import JSON_Serializer


def main():
    print("hello world")
    price = 500
    json_serializer = JSON_Serializer()
    json_str = json_serializer.dumps(price)
    print(json_str)
    buffer1 = json_serializer.loads(json_str)
    print(buffer1)

if __name__ == "__main__":
    main()
```

## Using as a console utility:
#### Simple example:

##### 1) Including '--src_file' and '--to_file' flags:
```
python3 -m matuamod_serializer --src_file 'all_data.json' --to_file 'all_data.toml'
```
##### 2) Including '--make_config' flag:

```
python3 -m matuamod_serializer --make_config 'config.ini'
```

#### config.ini:

```
[DEFAULT]
src_file = "all_data.json"
to_file = "all_data.yaml"
```

## Tests:
##### 1) Testing json_serializer.py:

```
python -m pytest test/json_test.py --cov=matuamod_serializer/serializer/json_serializer/
```

##### 2) Testing toml_serializer.py:

```
python -m pytest test/toml_test.py --cov=matuamod_serializer/serializer/toml_serializer/
```

##### 3) Testing yaml_serializer.py:

```
python -m pytest test/yaml_test.py --cov=matuamod_serializer/serializer/yaml_serializer/
```

### Changing objects for serialization/parse:
##### Edit objects in 'make_file_content.py' and run:

```
python make_file_content.py
```