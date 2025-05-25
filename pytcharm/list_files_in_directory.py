import os
import glob
from typing import Generator

def list_files(dir_path: str) -> Generator[str, None, None]:
	for file_path in glob.glob(f"{dir_path}/**/*", recursive=True):
		if os.path.isfile(file_path) and '__pycache__' not in file_path:
			yield file_path

def file_contents(files_only: Generator[str, None, None]) -> None:
	for file in files_only:
		with open(file, 'r', encoding='utf-8', errors='ignore') as filee:
			print(f"--------File: {file} Contents ------")
			for line in filee.readlines():
				print(line.rstrip())

def main() -> None:
	files_list = list_files("C:\\Users\\HP\\Desktop\\python_coding_practice")
	file_contents(files_list)
	# for file in files_list:

if __name__ == '__main__':
	main()

