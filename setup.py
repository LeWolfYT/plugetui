from cx_Freeze import setup, Executable

build_exe = {
    "packages": ['term', 'getch', 'pynput', 'cursor', 'requests', 'colorama'],
    'excludes':['PyQt4', 'PyQt5', 'PySide', 'PySide2', 'IPython', 'jupyter_client', 'jupyter_core', 'ipykernel', 'ipython_genutils', 'pytz', 'asyncio', 'pandas', 'psutil', 'numpy', 'pygments', 'scipy', 'openpyxl', 'matplotlib', 'docutils', 'sqlalchemy', 'sqlite3', 'tornado', 'libssl', 'pyportmidi', 'pycrypto', 'crypto', 'xmlrpc', 'macholib', 'pygame'],
}

setup(
    name="PluGet UI",
    version="0.0.1",
    author="LeWolfYT",
    author_email="ciblox3@gmail.com",
    description="A UI for PluGet (sidgames5/pluget!!!)",
    options={"build_exe": build_exe},
    executables=[Executable("plugetui.py")],
)