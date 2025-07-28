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
                sh "docker build -t ${IMAGE}:${TAG} ."
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
                sh "docker tag ${IMAGE}:${TAG} ${IMAGE}:latest"
                sh "docker push ${IMAGE}:${TAG}"
                sh "docker push ${IMAGE}:latest"
            }
        }

        stage('Jubin - Update kubeconfig') {
            steps {
                sh "aws eks update-kubeconfig --region us-east-2 --name EKS-CICD"
            }
        }

        stage('Jubin - Create Deployment if Not Exists') {
            when {
                expression {
                    def res = sh(
                        script: "kubectl get deployment jenkins-project -n jenkins-cicd > /dev/null 2>&1 || echo MISSING",
                        returnStdout: true
                    ).trim()
                    return res.contains("MISSING")
                }
            }
            steps {
                sh '''
                    echo "Deployment not found, creating a new one..."
                    kubectl create ns jenkins-cicd || true
                    kubectl apply -f k8s/deploy.yaml
                '''
            }
        }

        stage('Jubin - Deploy to EKS') {
            steps {
                sh """                        
                    echo "Deploying the new image to EKS..."
                    kubectl set image deployment/jenkins-project jenkins-project=${IMAGE}:${TAG} -n jenkins-cicd
                    
                    echo "Waiting for the deployment to complete..."
                    kubectl rollout status deployment/jenkins-project -n jenkins-cicd
                """
            }
        }
    }
}
