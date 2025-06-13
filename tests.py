from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

print(get_file_content("calculator", "main.py") + "\n")
print(get_file_content("calculator", "pkg/calculator.py") + "\n")
print(get_file_content("calculator", "/bin/cat") + "\n")