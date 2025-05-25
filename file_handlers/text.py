"""
This module is to handle simple text file
"""

def write_data(file_name: str, data: str) -> None:
    with open(file_name, 'a+') as text_file:
        text_file.write(f"{data} \n")

def read_data(file_name: str) -> list[str]:
    with open(file_name, 'r') as read_file:
        return read_file.readlines()

def main() -> None:
    data: str = "This is simple text file"
    write_data(r'test_text.txt', data)
    file_contents = read_data(r'test_text.txt')
    print(f"File contents are:\n {file_contents}")

if __name__ == '__main__':
    main()