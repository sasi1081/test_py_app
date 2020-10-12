pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
   /* stage('SCM') {
      steps {
       git 'https://github.com/sasi1081/test_py_app.git'
      }
    }*/

      stage('build') {
        steps {
          withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pip install --user -r requirements.txt'
          sh 'python -m py_compile app.py'
           stash(name: 'compiled-out' , includes: 'app.py')
          }
        }
      }
/*    stage('test') {
      agent {
        docker {
         image 'qnib/pytest'
        }
      }
      steps{
        sh 'py.test --verbose --junit-xml test-result/result.xml  test_flask.py'
        sh ' flake8 --statistics app.py test_flask.py --output-file flake.out'

      }
      
      post {
        always{
          junit 'test-result/result.xml'
        }
  }
} */
    stage('Final') {
      
      agent any 
      
      environment {
        
        VOL = '$(pwd)/:/'
        IMG = 'cdrx/pyinstaller-linux:python2'
      }
      
      steps {
        
        dir(path: env.BUILD_ID) {
          
          unstash(name: 'compiled-out')
          
          sh "docker run --rm -v ${VOL} ${IMG} 'pyinstaller -F app.py'"
        }
      }
      
      post {
        
        success {
          
          archiveArtifacts "${env.BUILD_ID}/src/app "
          sh "docker run --rm -v ${vVOL} ${IMG}  'rm -rf build dist'"
        
        }
      }
    
    
  }}
}
