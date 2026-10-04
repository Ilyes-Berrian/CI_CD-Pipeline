pipeline {
    // Run the pipeline on the Jenkins worker configured for Flask builds.
    agent { label 'flask-worker' }

    stages {
        // Check out the application source before running tests or building the image.
        stage('Clone git Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Ilyes-Berrian/CI_CD-Pipeline.git' 
                sh 'ls -l'
            }
        }

        // Install Python and pip on the worker so the test stage can install dependencies.
        stage('Setup Python Interpreter') {
            steps {
                sh 'yum install python3 python3-pip -y'
            }
        }

        // Install dependencies, run the test suite, and fail the build for lint violations.
        stage('Unit Test Cases & Lint Check') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'pytest'
                sh 'flake8 .'
            }
        }

        // Build the deployable image only after tests and linting have passed.
        stage('Build Docker Image') {
            steps {
                sh 'yum install docker -y'
                sh 'systemctl start docker'
                sh 'docker build -t flask-app:v1.0 .'
            }
        }

        // Replace any previous container with the newly built application image.
        stage('Deploy the Flask Webapp') {
            steps {
                sh 'docker rm -f flask-webapp'
                sh 'docker run -dit --name flask-webapp -p 8081:80 flask-app:v1.0'
            }
        }

        // Report a successful deployment in the Jenkins console.
        stage('Return Success Status') {
            steps {
                echo 'Flask Webapp Deployed Successfully!'
            }
        }

    }
}
