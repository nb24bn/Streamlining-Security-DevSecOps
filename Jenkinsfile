pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'docker build -t my-app .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'docker run my-app pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh 'docker-compose up -d'
            }
        }
    }
}
