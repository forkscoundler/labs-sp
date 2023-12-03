Jankins pipeline




pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    }
    stages {
        stage('Збірка RPM та DEB') {
            steps {
                script {
                    // Ваші команди для збірки RPM та DEB тут
                    sh 'echo "Збірка RPM та DEB"'
                }
            }
        }
        stage('Встановлення RPM або DEB') {
            steps {
                script {
                    // Ваші команди для встановлення тут
                    sh 'echo "Встановлення RPM або DEB"'
                }
            }
        }
        stage('Виконання скрипту') {
            steps {
                script {
                    // Ваша команда для виконання скрипту тут
                    sh './usr/bin/count_files.sh'
                }
            }
        }
    }
}