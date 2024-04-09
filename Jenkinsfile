// pipeline {
//     agent any 
//     stages {
//       stage("build") {
//         steps {
//           sh 'pip install -r requirements.txt'
//         }
//       }
//       stage("execute"){
//         steps {
//           sh 'python3 -m streamlit run goat.py'
//         }
//       }
//     }
//     post {
//         success {
//           echo "Pipeline completed successfully"
//         }
//     }
// }

pipeline {
    agent any 
    
    stages {
        stage("build") {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage("execute") {
            steps {
                sh 'python3 -m streamlit run goat.py'
            }
        }
        stage("finalize") {
            steps {
                script {
                    echo "Sleeping for 5 seconds"
                    sleep 5
                }
            }
        }
    }
    
    post {
        success {
            echo "Pipeline completed successfully"
            currentBuild.result = 'ABORTED'
        }
    }
}
