pipeline {
    agent any
    
    stages {
        stage('pre-run') {
            steps {
                sh 'chmod +x ./script/ *'
                sh 'echo "Hello World!"'
                sh 'touch Leeroy.txt'
            }
        }
    }
}