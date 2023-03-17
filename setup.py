from cx_Freeze import setup, Executable

base = None

executables = [Executable("files_copying_between_dirs.py", base=base)]

packages = ["idna", "sys", "os", "shutil"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="files_copying_between_dirs",
    options=options,
    version="0.1",
    description='script for copying files between directories with duplicates preserving',
    executables=executables
)
