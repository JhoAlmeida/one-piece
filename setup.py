import cx_Freeze

executables = [cx_Freeze.Executable(
    script="IronMan.py",
    icon="assets/ironIcon.ico"
)]
cx_Freeze.setup(
    name="IronMan",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }}
    ,executables = executables
)

