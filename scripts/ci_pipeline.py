import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        exit(1)

print("Running linting and static code analysis...")
run_command("pylint src/")

print("Running tests...")
run_command("pytest src/tests/")

print("Building Docker image...")
run_command("docker build -t devsecops-app .")

