## TWEETER MAN

### This is the backend repository for my ai generated threads app

Working with pyenv

```
brew update
brew install pyenv
```

Add the following lines to ~/.bashrc or ~/.zprofile

```
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Create the virtual env

```
pyenv install 3.9.12
pyenv virtualenv 3.9.12 tweeter
```

Activate virtualenv

```
pyenv activate tweeter
```

Start application

`uvicorn main:app --reload`

Close application

`ctrl + c`
