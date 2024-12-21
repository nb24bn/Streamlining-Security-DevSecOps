import os
import subprocess

def deploy_app():
    print("Deploying the application...")
    command = "docker-compose up -d"
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        print("Application deployed successfully!")
    else:
        print("Deployment failed.")

if __name__ == "__main__":
    deploy_app()

