pipeline {
    agent any

    stages {
        stage('Generate Data CSV') {
            agent { 
                docker { image 'python:3.9-slim' } 
            }
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                    sh 'python generate_fake_data.py'
                }
            }
        }
        
        stage('Run Postman Collection with Newman') {
            agent { 
                docker { image 'postman/newman' } 
            } 
            steps {
                script {
                    sh 'newman run exemple_reqrest.postman_collection.json -e jdd_env.json'
                }
            }
        }
    }
}
