# cookiecutter-lucode

A template for an R package using [lucode2](https://github.com/pik-piam/lucode2) to automate manual tasks.
Mostly useful if you want to create a package in the [PIK PIAM](https://github.com/pik-piam) universe.

## Instructions

To create a new project:
1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html).
2. Run `cookiecutter gh:pik-piam/cookiecutter-lucode` and answer all the questions.
3. Switch into the new directory, run `git init .`, `git add .`, and `git commit -m 'initial commit'` to create a git repo.
4. Create a new package at [github:pik-piam](https://github.com/pik-piam).
5. Add the github repository as your remote in git using `git remote add upstream https://github.com/pik-piam/<your_project>`.
6. Push your repo using `git push upstream main`.
7. Run `Rscript -e 'lucode2::buildLibrary()'` for the first time to get the latest configs for everything.
