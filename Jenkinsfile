pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = "heyitssubedi"
        FRONTEND_IMAGE = "heyitssubedi/frontend"
        BACKEND_IMAGE = "heyitssubedi/backend"
        GIT_COMMIT_HASH = ""
        BUILD_VERSION = ""
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/itkum101/project.git'
                    GIT_COMMIT_HASH = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    BUILD_VERSION = "build-${env.BUILD_NUMBER}-${GIT_COMMIT_HASH}"
                }
            }
        }

        stage('Docker Login') {
            steps {
                script {
                    // Using Jenkins credentials for Docker Hub login
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_ACCESS_TOKEN')]) {
                        sh "echo $DOCKER_HUB_ACCESS_TOKEN | docker login -u $DOCKER_HUB_USERNAME --password-stdin"
                    }
                }
            }
        }
 stage('Build and Push Backend') {
    steps {
        script {
            // Build backend service using Docker Compose
            sh "docker-compose build backend"
            
            // Push the image directly without tagging
            sh "docker push $(docker-compose images -q backend)"
        }
    }
}

stage('Build and Push Frontend') {
    steps {
        script {
            // Build frontend service using Docker Compose
            sh "docker-compose build frontend"
            
            // Push the image directly without tagging
            sh "docker push $(docker-compose images -q frontend)"
        }
    }
}





        stage('Deploy') {
            steps {
                script {
                    sh "docker-compose down"
                    sh "docker-compose pull"
                    sh "docker-compose up -d"
                }
            }
        }
    }
}
