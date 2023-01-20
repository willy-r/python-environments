# Python Environments - Dependecy & Workspace management


## Installing Python

- Use [`pyenv`](https://github.com/pyenv/pyenv) for switch between Python versions without effort.

### Commands

- After you have it installed, you can easily install a specific version of Python:
```bash
$ pyenv install 3.8.5
$ pyenv install 3.8.6
$ pyenv install 3.9.0
$ pyenv install 3.10.2

$ pyenv versions
* system
  3.8.5
  3.8.6
  3.9.0
  3.10.2
```

- You can set a "global" Python version to use at any place of your system:
```bash
$ pyenv global 3.8.6

$ pyenv versions
  system
  3.8.5
* 3.8.6 (set by /home/will/.pyenv/version)
  3.9.0
  3.10.2

$ python -V
Python 3.8.6
```
> This will not alter anything of your system Python.

- You can also set a "local" Python version to use at your current work directory, like so:
```bash
$ pyenv local 3.10.2

$ pyenv versions
  system
  3.8.5
  3.8.6
  3.9.0
* 3.10.2 (set by /home/will/Documents/studies/about-python-environments/.python-version

$ python -V
Python 3.10.2
```
> A file called `.python-version` will be created to pyenv identify which version of Python you are using at the moment. You can add this file on your .gitignore as well.


## Managing Dependencies

Tools for managing Python dependencies and virtual environment.

### venv + pip

- Using `venv` and `pip` is the simplest way of creating a virtual environment to get things done quickly. They already come installed with the most versions of Python, so you don't need to install anything.

#### Usage

1. To create a new virtual environment called **venv** you can just do:
```bash
$ python -m venv venv
```

2. With the created virtual environment you still need to activate it with the command:
```bash
$ source venv/bin/activate
(venv)$
(venv)$ deactivate # Deactivate the virtual environment
```

3. You can check which Python interpreter the system are appointing to and it will be the Python interpreter of the virtual environment:
```bash
(venv)$ which python
/home/will/Documents/studies/about-python-environments/venv/bin/python
```

4. With that, you can install packages local to your projects with `pip` inside your virtual environment:
```bash
(venv)$ pip install requests
...
```

5. To things working properly, you need a track of each dependency you need to install to run the project, usually you need a file called `requirements.txt` inside of the root directory of your project. You can manually create one, or just create with `pip freeze`
```bash
(venv)$ python -m pip freeze > requirements.txt
(venv)$ cat requirements.txt
certifi==2022.12.7
charset-normalizer==3.0.1
idna==3.4
requests==2.28.2
urllib3==1.26.14
```
> To only get top-level dependecy (requests==2.28.2), you can check pip-chill for that.

- It's great and easy, but we have a problem: we need to manage each `requirements.txt` depending on the environment we are in, for example a `requirements.txt` with the prod packages and a `requirements.dev.txt` with packages that we only use on development.


### poetry

- `poetry` is the most feature-rich dependency management tool for Python, it comes with a powerful CLI to create and manage Python projects.

- Since Poetry is a more complicated too to use, I do recommend reading the [oficial docs](https://python-poetry.org/docs/) about it, it's easy when you get it.


#### Usage

@TODO
