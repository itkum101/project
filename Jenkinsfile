pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = "heyitssubedi"
        FRONTEND_IMAGE = "heyitssubedi/frontend"
        BACKEND_IMAGE = "heyitssubedi/backend"
        KUBECONFIG = '/var/jenkins_home/kubeconfig' // Best practice: Store in Global Credentials.
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Perform a shallow clone for faster retrieval of the latest commit
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
                            // Build the backend service using Docker Compose
                            sh "docker-compose build backend"
                        }
                    }
                }

                stage('Build Frontend') {
                    steps {
                        script {
                            // Build the frontend service using Docker Compose
                            sh "docker-compose build frontend"
                        }
                    }
                }
            }
        }

        stage('Prune Images') {
            steps {
                script {
                    // Remove unused Docker images to free up space
                    sh "docker image prune -f"
                }
            }
        }

        stage('Docker Login') {
            steps {
                script {
                    // Authenticate to Docker Hub using Jenkins credentials
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_ACCESS_TOKEN')]) {
                        sh "echo $DOCKER_HUB_ACCESS_TOKEN | docker login -u $DOCKER_HUB_USERNAME --password-stdin"
                    }
                }
            }
        }

        stage('Push Images') {
            parallel {
                stage('Push Backend') {
                    steps {
                        script {
                            // Tag and push the backend image
                            sh 'docker tag $(docker images -q heyitssubedi/backend:latest) $BACKEND_IMAGE:latest && docker push $BACKEND_IMAGE:latest'
                        }
                    }
                }

                stage('Push Frontend') {
                    steps {
                        script {
                            // Tag and push the frontend image
                            sh 'docker tag $(docker images -q heyitssubedi/frontend:latest) $FRONTEND_IMAGE:latest && docker push $FRONTEND_IMAGE:latest'
                        }
                    }
                }
            }
        }

        // stage('Deploy to Kubernetes') {
        //     steps {
        //         script {
        //             // Apply Kubernetes configurations
        //             sh '''
        //             kubectl delete -f deployment.yaml
        //             kubectl apply -f deployment.yaml
        //             kubectl apply -f namespace.yaml
        //             kubectl apply -f secret-and-config.yaml
        //             kubectl apply -f service.yaml
        //             kubectl apply -f argocd.yaml
        //             '''
        //         }
        //     }
        // }
    }
}
