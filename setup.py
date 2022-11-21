import cx_Freeze

executables = [cx_Freeze.Executable(
    script="onePiece.py",
    icon="one-piece/icon.ico"
)]
cx_Freeze.setup(
    name="OnePiece",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["one-piece"]
        }}
    ,executables = executables
)

