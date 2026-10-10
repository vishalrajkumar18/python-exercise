import subprocess
# imports subprocess module to execute system commands
# runs the external system command 'ls -l'
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# displays standard output from the external command
print(result.stdout)
