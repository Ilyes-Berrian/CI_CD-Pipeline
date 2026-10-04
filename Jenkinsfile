pipeline { //Flask HelloWorld Webapp Pipeline
    agent { label 'flask-worker' } //This is the label of the node where the pipeline will run

    stages {
        stage('Clone git Repo') { //Job1
            steps {
                git branch: 'main', url: 'https://github.com/Ilyes-Berrian/CI_CD-Pipeline.git' 
            }
        }

        stage('Setup Python Interpreter') {//Job2
            steps {
                sh 'yum install python3 python3-pip -y'
            }
        }

        stage('Unit Test Cases & Lint Check') {//Job3
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'pytest'
                sh 'flake8'
            }
        }

        stage('Build Docker Image') {//Job4
            steps {
                sh 'yum install docker -y'
                sh 'systemctl start docker'
                sh 'docker build -t flask-app:v1.0 .'
            }
        }

        stage('Deploy the Flask Webapp') {//Job4
            steps {
                sh 'docker rm -f flask-webapp'
                sh 'docker run -dit --name flask-webapp -p 8081:80 flask-app:v1.0'
            }
        }

        stage('Return Success Status') {//Job5
            steps {
                echo 'Flask Webapp Deployed Successfully!'
            }
        }

    }
}
