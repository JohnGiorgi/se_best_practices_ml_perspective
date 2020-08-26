## Linting

A linter is a tool that can automatically identify syntax and stylistic errors in your code. A very popular linter for python is [`flake8`](https://flake8.pycqa.org/en/latest/) and will be our tool of choice in this guide.

First, make sure we are in our project directory (named `"se-best-practices-ml-perspective"`) by default. Then, lets add `flake8` as a development dependency.

``` bash
poetry add --dev flake8
```

`--dev` just means we want this to be a _development dependency_, that is, a dependency we need to develop our code, but _not_ required by an end user who simply wants to run our code. Lets check our `pyproject.toml`.

``` toml hl_lines="14"
[tool.poetry]
name = "se-best-practices-ml-perspective"
version = "0.1.0"
description = ""
authors = ["johngiorgi <johnmgiorgi@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.7"
pytorch-lightning = "^0.9.0"
torchvision = "^0.7.0"

[tool.poetry.dev-dependencies]
pytest = "^5.2"
flake8 = "^3.8.3"

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```

As expected, `flake8` has been added as a development dependency.

Now, lets setup a simple example with `pytorch-lightning`. We will borrow [their minimal example](https://github.com/PyTorchLightning/pytorch-lightning#heres-a-minimal-example-without-a-test-loop). Download it from this repository.

``` bash
curl 
```

Then, lets lint the file, checking it for errors.

```
poetry run flake8 .
```

`flake8` reports several sytlistic errors

```
./se_best_practices_ml_perspective/main_with_stylistic_errors.py:1:80: E501 line too long (90 > 79 characters)
./se_best_practices_ml_perspective/main_with_stylistic_errors.py:28:1: W293 blank line contains whitespace
./se_best_practices_ml_perspective/main_with_stylistic_errors.py:40:1: E305 expected 2 blank lines after class or function definition, found 1
./se_best_practices_ml_perspective/main_with_stylistic_errors.py:41:80: E501 line too long (80 > 79 characters)
./se_best_practices_ml_perspective/main_with_stylistic_errors.py:46:59: W292 no newline at end of file
```

Of course, we could fix each error manually, but in the next section, we will see how a code formatter can automatically fix them for us!


Now, lets create a python file, `main.py` under our packages root folder (`"se-best-practices-ml-perspective/se-best-practices-ml-perspective"` by default)

```bash
touch se_best_practices_ml_perspective/main.py
```

Then, lets add a simple `sklearn` classifier to `main.py`

``` python

if __name__ == "__main__":
    main()
```