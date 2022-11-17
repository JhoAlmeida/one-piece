import cx_Freeze

executables = [cx_Freeze.Executable(
    script="OnePiece.py",
    icon="assets/icon.png"
)]
cx_Freeze.setup(
    name="OnePiece",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }}
    ,executables = executables
)

