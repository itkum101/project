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
                    // Use shallow clone for faster Git cloning (only latest commit)
                    git(
                        branch: 'main',
                        url: 'https://github.com/itkum101/project.git',
                        depth: 1
                    )
                }
            }
        }


 stage('Build Services') {
            parallel {
                stage('Build Backend') {
                    steps {
                        script {
                            // Build backend service using Docker Compose
                            sh "docker-compose build backend"
                        }
                    }
                }

                stage('Build Frontend') {
                    steps {
                        script {
                            // Build frontend service using Docker Compose
                            sh "docker-compose build frontend"
                        }
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh "docker-compose down"
                    sh "docker-compose up -d"
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
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_ACCESS_TOKEN')]) {
                        sh "echo $DOCKER_HUB_ACCESS_TOKEN "
                    }
                    
                }
            }
        }

 stage(' Push Backend') {
    steps {
        script {

            
            // Push the image directly without tagging
           sh 'docker tag $(docker images -q backend) $BACKEND_IMAGE:latest && docker push $BACKEND_IMAGE:latest'

        }
    }
}

stage(' Push Frontend') {
    steps {
        script {
            
            // Push the image directly without tagging
             sh 'docker tag $(docker images -q frontend) $FRONTEND_IMAGE:latest && docker push $FRONTEND_IMAGE:latest'

        }
    }
}








    }
}
