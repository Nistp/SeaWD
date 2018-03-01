import yaml
import toml

# TODO: pick yaml parser
# TODO: research PIPENV <<<

d = {
    'lol' : 'wut',
    'cmon': 'wokrwokr!',
    'keys' : ['vals','vals2','vals3']
    }

global_config = {}
yaml_config = '.sewd_conf.yaml'
toml_config = '.sewd_conf.toml'



def read_yaml_config(path_to_config):
    with open(path_to_config, 'r') as f:
        conf = yaml.safe_load(f) 
    return conf 

def write_yaml_config(config, path_to_config):
    with open(path_to_config, 'w') as f:
        yaml.dump(config, f)


def read_toml_config(path_to_config):
    with open(path_to_config, 'r') as f:
        conf = toml.load(f) 
    return conf 

def write_toml_config(config, path_to_config):
    with open(path_to_config, 'w') as f:
        toml.dump(config, f)


def test_yaml_toml():
    write_yaml_config(d, path_to_config=yaml_config) 
    global_config = read_yaml_config(path_to_config=yaml_config)
    print(global_config)

    write_toml_config(d, path_to_config=toml_config) 
    global_config = read_toml_config(path_to_config=toml_config)
    print(global_config)



global_config = read_toml_config(path_to_config=toml_config)
print(global_config)
global_config = read_yaml_config(path_to_config=yaml_config)
print(global_config)
