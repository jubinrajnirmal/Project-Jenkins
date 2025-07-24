pipeline {
    agent any
    environment {
        CREDENTIALS = 'dockerhub'
        IMAGE = 'jubinraj/jenkins-project'
        TAG = "v${BUILD_NUMBER}"
    }
    stages {
        stage('Jubin - Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE}:${TAG} ."
                }
            }
        }
        stage('Jubin - Login to Dockerhub') {
            steps {
                withCredentials([usernamePassword(credentialsId: CREDENTIALS, passwordVariable: 'pwd', usernameVariable: 'user')]) {
                    sh "echo ${pwd} | docker login -u ${user} --password-stdin"
                }
            }
        }
        stage('Jubin - Push Image to Dockerhub') {
            steps {
                script {
                    sh "docker tag ${IMAGE}:${TAG} ${IMAGE}:latest"
                    sh "docker push ${IMAGE}:${TAG}"
                    sh "docker push ${IMAGE}:latest"
                }                
            }
        }
    }
}