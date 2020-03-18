pipeline {
    agent any
    stages {
        stage('Development Environment') {
            steps {
                sh 'chmod +x ./script/*'
                sh './script/before_install.sh'


                sh 'sudo systemctl daemon-reload'
                sh 'sudo systemctl enable flask.service'
                sh 'sudo systemctl restart flask.service'
                sh 'sleep 15'
                sh 'echo "successful build!"'
            }
        }
        stage('Testing'){
            steps{
                sh './script/tester.sh'
                sh 'python3 -m pytest ./tests/testing.py'
                sh 'python3 -m coverage run -m pytest ./tests/testing.py'
                sh 'python3 -m coverage report -m'
                sh 'echo "Testing Successful!"'
                
            }
        }
    }
}