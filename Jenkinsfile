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
                }            
            }
        }
        
        stage('Run Postman Collection with Newman') {
            agent { 
                docker { 
                    image 'postman/newman' 
                    args '--entrypoint=""' 
                }
            }
            steps {
                script {
                    sh 'npm install --prefix ./node_modules allure-commandline --save-dev'

                    sh '''
                    ls -lah
                    newman run exemple_reqrest.postman_collection.json     -e Mon_api.postman_environment.json     --iteration-data jdd.json --reporters cli,allure --reporter-allure-export allure-results
                    '''
                    sh 'allure generate allure-results --clean -o allure-report'
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                        def allureResultsDir = 'allure-results'
                        def allureReportDir = 'allure-report'
                        sh "allure serve ${allureResultsDir} --report-dir ${allureReportDir}"
                    }
                }
            }
        }
    

    post {
        always {
            cleanWs()  
        }
    }
}
