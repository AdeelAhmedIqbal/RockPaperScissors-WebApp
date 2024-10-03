pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'rockpaperscissors-webapp:latest'  // Docker image name
        SONARQUBE_URL = 'http://localhost:9000'  // Adjust to your SonarQube URL
        SELENIUM_TEST_SCRIPT = 'selenium_test.py'  // Path to the Selenium test script
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image for the project...'
                // Build the Docker image
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                
                // Start the Docker container for testing
        	sh '''
        	docker stop rockpaperscissors || true
        	docker rm rockpaperscissors || true
       	docker run -d -p 80:80 --name rockpaperscissors $DOCKER_IMAGE
        	'''

                // HTML validation using tidy
                sh '''
                tidy -errors -q index.html
                '''
                // Install python dependencies
                sh '''
                pip install -r requirements.txt
                '''

                // Run Selenium Tests
                echo 'Running Selenium tests...'
                sh '''
                
                # Run the Selenium test (assuming a Python-based Selenium test)
                python3 $SELENIUM_TEST_SCRIPT
                '''
                
                // Stop and remove the container after tests
        	sh '''
        	docker stop rockpaperscissors
        	docker rm rockpaperscissors
        	 '''
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo 'Running SonarQube analysis...'
                sh 'echo $PATH'
                sh 'which sonar-scanner' 
                withSonarQubeEnv('SonarQube') {
                    def scannerHome = tool: 'SonarQube-Scanner'
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=rockpaperscissors-webapp \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=$SONARQUBE_URL \
                      -Dsonar.login=squ_b35960057e845d1b471468b0fa09dac62bdf4987
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Docker container...'
                // Stop and remove any existing container, then run the new one
                sh '''
                docker stop rockpaperscissors || true
                docker rm rockpaperscissors || true
                docker run -d -p 80:80 --name rockpaperscissors $DOCKER_IMAGE
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for errors.'
        }
    }
}
