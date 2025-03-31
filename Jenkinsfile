pipeline {
    agent none

    stages {
        stage('Generate Data CSV') {
            agent { label 'python-agent' } 
            steps {
                script {
                    sh 'pip install -r requirements.txt'

                    sh 'python generate_fake_data.py'
                }
            }
        }
        
        stage('Run Postman Collection with Newman') {
            agent { label 'newman-agent' } 
            steps {
                script {
                    sh 'newman run exemple_reqrest.postman_collection.json -e jdd.csv'
                }
            }
        }
    }
}
