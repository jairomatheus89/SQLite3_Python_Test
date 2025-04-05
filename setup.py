from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["colorama"],
    "include_files": []
}

setup(
    name="JairoDataBase",
    version="0.1",
    description="App to reg/read usernames into sqlite3",
    options={"build_exe": build_exe_options},
    executables=[Executable("runApp.py")]
)