# cookiecutter-lucode

A template for an R package using [lucode2](https://github.com/pik-piam/lucode2) to automate manual tasks.
Mostly useful if you want to create a package in the [PIK PIAM](https://github.com/pik-piam) universe.

## Instructions

To create a new project:

**Install cookiecutter**

[Install cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html) if you don't have it already.

**Generate the basic files**

In the terminal, run `cookiecutter gh:pik-piam/cookiecutter-lucode` and answer all the questions.

**Create a git repository**

If you use the terminal, switch into the new directory and run `git init .; git add .; git commit -m 'initial commit'` to create a git repo.

**Create and populate github repository**

This is easiest using the [`gh` command line tool](https://cli.github.com/). If you have it installed and
configured, you can create the repository under the `pik-piam` name space, push the files you have so far,
and create an own fork using the terminal:
```
gh repo create --public --push --source . pik-piam/<your package name>
gh repo fork
```

Alternatively, you can do this all with the github web interface and the terminal:
1. Create a new repository via the web interface at [github:pik-piam](https://github.com/organizations/pik-piam/repositories/new).
2. Add the github repository as your remote in git using `git remote add upstream https://github.com/pik-piam/<your_project>`.
3. Push your repo using `git push upstream main`.
4. Create a fork of the repository at the repository's web page.
5. Add this fork to your repo using `git remote add origin https://github.com/<your username>/<your project>`

**Run buildLibrary for the first time**

Run `Rscript -e 'lucode2::buildLibrary()'` for the first time to get the latest configs for everything.
