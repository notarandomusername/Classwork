mkdir new-repo
cd new-repo
git init
git status
touch pumpkin.py
touch README.md
git status
git add .
git status
git commit -m "Created pumpkin and readme."
git config --global user.email "notanotherrandomusername@gmail.com"
git config --global user.name "Adam Szyluk"
git commit -m "Created pumpkin and readme."
git status
git commid -am "Updated files."
git commit -am "Updated files."
touch index.html
touch style.css
touch application.js
git commit -am "Added front-end for website."
git add .
git commit -m "Added front-end for website."
touch server.rb
git add .
git commit -m "Added server file."
git log
q
cd intro-to-lists
git commit -am "Modified exercise 2."
git commit -am "Modified exercise 3."
git commit -am "Modified exercise 4."
cd more-lists
git push -u origin master
git remote add myrepo https://github.com/notarandomusername/more-lists
git push myrepo master
