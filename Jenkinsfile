pipeline {
  agent any 
    stages {
      stage("build") {
        steps {
          sh 'pip install -r requirements.txt'
        }
      }
      stage("execute"){
        steps {
          sh 'python3 -m streamlit run goat.py'
        }
      }
      post {
        success {
          echo "Pipeline completed successfully"
        }
    }
}
