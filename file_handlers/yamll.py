import yaml
from datetime import datetime


def write_yaml_file(file_name: str, data_input: dict) -> None:
    with open(file_name, 'a+') as write_yaml:
        yaml.dump(data_input, write_yaml)

def read_yaml_file(file_name: str) -> None:
    with open(file_name, 'r') as read_yaml:
        data: dict = yaml.safe_load(read_yaml)
    return data

def main() -> None:
    data: dict = {'names': ['lucky', 'vicky', 'venky']}
    # write_yaml_file(data)
    date_and_time: datetime = datetime.now()
    data: dict = {'time': f'{date_and_time:%c}'}
    write_yaml_file(r'C:\Users\HP\Desktop\python_coding_practice\test.yaml', data)
    yaml_data = read_yaml_file(r'C:\Users\HP\Desktop\python_coding_practice\test.yaml')
    print(yaml_data)

if __name__=='__main__':
    main()