pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Build is successful'

            }
        }
        stage('Test') {
            steps {
                sh 'py.test testcases/test_practicePage.py'
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver Stage : py.test testcases/test_practicePage.py'
            }
        }
    }
    post {
        always {
             echo 'Testing'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
