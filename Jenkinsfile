pipeline {
    agent any
    stages {
        stage('1. Checkout') {
            steps {
                echo 'Stage 1: Checking out Calendar application source code'
                checkout scm
            }
        }
        stage('2. Build') {
            steps {
                echo 'Stage 2: Checking Python syntax'
                bat '"C:\\Users\\ANCY LAZAR\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m py_compile app.py'
                bat '"C:\\Users\\ANCY LAZAR\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m py_compile test_app.py'
            }
        }
        stage('3. Unit Testing') {
            steps {
                echo 'Stage 3: Running Calendar unit tests'
                bat '"C:\\Users\\ANCY LAZAR\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m unittest -v'
            }
        }
        stage('4. Integration Testing') {
            steps {
                echo 'Stage 4: Verifying Calendar module integration'
                bat '"C:\\Users\\ANCY LAZAR\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -c "from app import Calendar; c=Calendar(); e=c.add_event(\'Meeting\', \'2026-11-05\', \'10:00\'); assert c.edit_event(e[\'id\'], \'Review\', \'2026-11-06\', \'11:00\'); assert c.delete_event(e[\'id\']); print(\'Integration test passed\')"'
            }
        }
        stage('5. Package') {
            steps {
                echo 'Stage 5: Packaging Calendar source files'
                bat '"C:\\Users\\ANCY LAZAR\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -c "import zipfile; z=zipfile.ZipFile(\'calendar-app.zip\', \'w\'); z.write(\'app.py\'); z.write(\'test_app.py\'); z.close(); print(\'Package created successfully\')"'
            }
        }
        stage('6. Deploy') {
            steps {
                echo 'Stage 6: Preparing Calendar application deployment'
                bat 'if not exist deployment mkdir deployment'
                bat 'copy /Y app.py deployment\\app.py'
            }
        }
        stage('7. Verify Deployment') {
            steps {
                echo 'Stage 7: Verifying deployed application'
                bat '"C:\\Users\\ANCY LAZAR\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m py_compile deployment\\app.py'
                echo 'Calendar application deployment verification successful'
            }
        }
    }
    post {
        success {
            echo 'SUCCESS: All seven pipeline stages completed!'
        }
        failure {
            echo 'FAILURE: Check the Jenkins Console Output for errors.'
        }
    }
}

