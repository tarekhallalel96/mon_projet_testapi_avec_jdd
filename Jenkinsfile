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
        agent { 
            docker { 
                image 'postman/newman' 
                args '--entrypoint=""' 
            } 
}
steps {
    script {
        sh 'npm install --prefix ./node_modules allure-commandline --save-dev'
        
        // Lister les fichiers et exécuter la collection Postman avec Newman
        sh '''
        ls -lah
        newman run exemple_reqrest.postman_collection.json -e jdd.json --reporters cli,allure --reporter-allure-export allure-results
        '''
    }
}


            
        }

                stage('Generate Allure Report') {
            steps {
                script {
                    // Vérifiez si Allure est installé et générez le rapport
                    if (sh(script: "command -v allure", returnStatus: true) == 0) {
                        sh "allure serve ${ALLURE_RESULTS_DIR} --report-dir ${ALLURE_REPORT_DIR}"
                    } else {
                        echo "Allure not installed, skipping report generation"
                    }
                }
            }
        }


    }

        post {
        always {
            cleanWs()  // Nettoyer l'espace de travail après chaque exécution
        }
    }
}
