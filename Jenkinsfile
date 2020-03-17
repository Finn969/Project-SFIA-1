pipeline {
    agent any
    stages {
        stage('Development Environment') {
            steps {
                sh 'chmod +x ./script/*'
                sh './script/before_install.sh'

                sh 'sudo systemctl daemon-reload'
                sh 'sudo systemctl enable flask.service'
                sh 'sudo systemctl start flask.service'
                sh 'echo "successful build!"'
            }
        }
        stage('Testing'){
            steps{
                sh 'python3 -m pytest ./tests/testing.py'
                sh 'echo "Testing Successful!"'
                
            }
        }
    }
}