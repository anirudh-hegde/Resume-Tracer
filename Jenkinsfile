pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        checkout([$class: 'GitSCM', 
                                  branches: [[name: '*/main']], 
                                  userRemoteConfigs: [[url: 'https://github.com/anirudh-hegde/Resume-Tracer.git']]])
        script {
          sh 'pip install -r requirements.txt'
        }

      }
    }

    stage('test') {
      steps {
        sh 'python3 -m pytest -v'
      }
    }

    stage('deploy') {
      steps {
        sh 'python3 -m streamlit run goat.py &'
        sleep(time: 25, unit: 'SECONDS')
        sh 'pkill -f "python3 -m streamlit run goat.py"'
      }
    }

  }
}
