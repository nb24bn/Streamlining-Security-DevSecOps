pipeline {
    agent any  // Use any available agent, instead of running inside a Docker container

    environment {
        REGISTRY = 'docker.io'
        IMAGE_NAME = 'nabilabanu/devsecops-app' // Repository name on Docker Hub
        TAG = 'latest' // Version tag
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${TAG} .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm ${IMAGE_NAME}:${TAG} pytest'
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
                aquasec/trivy:latest image --no-progress ${IMAGE_NAME}:${TAG}
                '''
            }
        }

        stage('Push to Docker Registry') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-password', variable: 'DOCKER_PASSWORD')]) {
                    sh '''
                    echo "$DOCKER_PASSWORD" | docker login -u "NabilaBanu" --password-stdin $REGISTRY
                    docker tag ${IMAGE_NAME}:${TAG} $REGISTRY/${IMAGE_NAME}:${TAG}
                    docker push $REGISTRY/${IMAGE_NAME}:${TAG}
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                echo "Deploying application..."
                # Add deployment steps here, e.g., updating Kubernetes or Docker Swarm
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        failure {
            echo 'Pipeline execution failed.'
        }
    }
}
