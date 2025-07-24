pipeline {
    agent any
    environment {
        CREDENTIALS = 'dockerhub'
        IMAGE = 'jubinraj/jenkins-project:latest'
    }
    stages {
        stage('Jubin - Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE .'
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
                sh 'docker push $IMAGE'
            }
        }
    }
    
}