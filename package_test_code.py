from file_handlers import handler, write_yaml_file, write_data, read_data, read_yaml_file

from datetime import datetime

CURRENT_TIME = datetime.now()

handler()

def write_text_data() -> None:
    write_data(rf'text_file_{CURRENT_TIME:%y-%m-%d}.txt', f"This is the test message at: {CURRENT_TIME:%c}")
    print("Written the data successfully")
    
def read_text_data() -> list[str]:
    file_contents: list[str] = read_data(rf'text_file_{CURRENT_TIME:%y-%m-%d}.txt')
    for line in file_contents:
        print(line.title())

def write_yaml_data() -> None:
    data: dict = {'time': f"{CURRENT_TIME:%c}", 'countries': ['India', 'AUS', 'USA', 'UK']}
    write_yaml_file(rf'yaml_file_{CURRENT_TIME:%y-%m-%d}.yaml', data)
    print('yaml data written successfully')

def read_yaml_data() -> dict:
    file_contents: dict = read_yaml_file(rf'yaml_file_{CURRENT_TIME:%y-%m-%d}.yaml')
    print(f"yaml file contents are: {file_contents}")
            
def main() -> None:
    write_text_data()
    read_text_data()
    write_yaml_data()
    read_yaml_data()

if __name__ == "__main__":
    main()


