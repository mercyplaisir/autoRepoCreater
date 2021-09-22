AUTOREPOCREATER
----------------------

It automatically create a folder and a repository in github 

create a custom command in shell and create a function.

function create(){
  cd /home/mercy/Github
  mkdir $1
  cd $1
  touch README.md
  mkdir src && touch src/main.py
  #git init .
  #git add .
  #git commit -m "first commit"
  #git branch -M main
  #now it's time for webscraping to get remote

  subl .

}


