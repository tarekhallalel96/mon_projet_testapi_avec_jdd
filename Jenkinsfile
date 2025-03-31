pipeline {
    agent any

    stages {
        stage('Generate Data CSV') {
            agent { 
                docker {
                image 'python:3.9-slim'

                       }

            }
            steps {
                script {
                    sh '''
                    python3 -m venv venv
                    venv/bin/pip install --no-cache-dir -r requirements.txt
                    venv/bin/python jdd_faker.py
                    '''
                }            }
        }
        
        stage('Run Postman Collection with Newman') {
        agent { docker { image 'postman/newman' args '--entrypoint=' } }
            steps {
                script {
                    sh '''
                    ls -lah
                    newman run exemple_reqrest.postman_collection.json -e jdd.json
                    '''               
                     }
            }
        }
    }
}
