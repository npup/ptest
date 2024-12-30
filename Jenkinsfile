pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Code Format Check') {
            steps {
                sh '. .venv/bin/activate && black --check .'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pytest tests/ -v'
            }
        }
    }

    post {
        failure {
            emailext (
                subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                body: "Something is wrong with ${env.BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
        }
    }
}