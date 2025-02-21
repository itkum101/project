pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = "heyitssubedi"
        FRONTEND_IMAGE = "heyitssubedi/frontend"
        BACKEND_IMAGE = "heyitssubedi/backend"
 
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/itkum101/project.git'
                }
            }
        }


        stage('Deploy') {
            steps {
                script {
                    sh "docker-compose down"
                    sh "docker-compose up --build"
                }
            }
        }
    }
}
