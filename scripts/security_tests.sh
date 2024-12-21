#!/bin/bash

echo "Running Bandit for static code analysis..."
bandit -r src/

echo "Running Trivy for container scanning..."
trivy image devsecops-app

