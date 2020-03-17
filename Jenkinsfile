pipeline {
    agent any
    stages {
        stage('Development Environment') {
            steps {
                sh 'chmod +x ./script/*'
                sh './script/before_install.sh'
                sh './script/installation.sh'
                sh 'sudo systemctl start flask.service'
            }
        }
        stage('Testing'){
            steps{
                sh 'pytest ./tests/testing.py'
                sh 'echo "Testing Successful!"'
                
            }
        }
    }
}