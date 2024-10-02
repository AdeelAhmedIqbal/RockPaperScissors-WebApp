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
            }
        }

        stage('Code Quality Analysis') {
    steps {
    	echo 'Running SonarQube analysis...'
        script {
            // Use SonarQube server configured in Jenkins and run SonarQube analysis
            withSonarQubeEnv('SonarQube') {  
                // Retrieve the SonarQube token from Jenkins credentials
                withCredentials([string(credentialsId: 'SonarQube Token', variable: 'SONAR_TOKEN')]) {
                    sh '''
                    sonar-scanner \
                        -Dsonar.projectKey=rockpaperscissors-webapp \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=$SONARQUBE_URL \
                        -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }

        // wait for the SonarQube Quality Gate results and fail the pipeline if not passed
        script {
            waitForQualityGate abortPipeline: true
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
