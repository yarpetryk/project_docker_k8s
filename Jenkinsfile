pipeline {
    agent any
    stages {
        stage('Run automated test') {
            steps {
                echo 'Pipeline is running...'
                sh 'docker compose up --abort-on-container-exit --build'
            }
        }
    }
    post {
        always {
            echo 'Pipeline is triggered successfully'
        }
        success {
            echo 'Pipeline runs with SUCCESS'
        }
        failure {
            echo 'Pipeline runs with FAILURE'
//             mail to: 'yaroslav.petryk@lembergsolutions.com',
//                  subject: "Pipeline finished with failure",
//                  body: "ERROR!!!"
        }
    }
}