application_title = "Word Guessing Game"
main_python_file = "wordGuessing.py"
include_files = "dictionary.txt"
your_name = "Luke Reynolds"
program_description = "A simple word guessing game built in python"

#main
import sys

from cx_Freeze import setup, Executable

base = None
	
setup(
	name=application_title,
	version="1.0",
	description=program_description,
	author=your_name,
	options={"build_exe":{"include_files":include_files}},
		executables=[Executable(main_python_file, base=base)]
)
