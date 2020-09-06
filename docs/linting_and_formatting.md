## Linting

A linter is a tool that can automatically identify syntax and stylistic errors in your code. A very popular linter for python is [`flake8`](https://flake8.pycqa.org/en/latest/) and will be our tool of choice in this guide.

First, make sure we are in our project directory (named `se_best_practices_ml_perspective`) by default. Then, lets add `flake8` as a development dependency.

``` bash
poetry add --dev flake8
```

!!! note
    `--dev` just means we want this to be a _development dependency_, that is, a dependency we need to develop our code, but _not_ required by an end user who simply wants to run our code. Lets check our `pyproject.toml`.

``` toml hl_lines="14"
[tool.poetry]
name = "se_best_practices_ml_perspective"
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

Now, lets setup a simple example with `pytorch-lightning`. We will borrow [their minimal example](https://github.com/PyTorchLightning/pytorch-lightning#heres-a-minimal-example-without-a-test-loop). Download it by running the following.

``` bash
curl -o se_best_practices_ml_perspective/main.py https://raw.githubusercontent.com/JohnGiorgi/se_best_practices_ml_perspective/master/se_best_practices_ml_perspective/main_with_stylistic_errors.py
```

Then, lets lint the file, checking it for errors.

```
poetry run flake8 .
```

`flake8` reports several sytlistic errors

```
./se_best_practices_ml_perspective/main.py:1:80: E501 line too long (90 > 79 characters)
./se_best_practices_ml_perspective/main.py:28:1: W293 blank line contains whitespace
./se_best_practices_ml_perspective/main.py:40:1: E305 expected 2 blank lines after class or function definition, found 1
./se_best_practices_ml_perspective/main.py:41:80: E501 line too long (80 > 79 characters)
./se_best_practices_ml_perspective/main.py:46:59: W292 no newline at end of file
```

Now, we could fix each error manually, but in the next section, we will see how a code formatter can automatically fix them for us!

## Code Formatting

A code formatter is a tool that will ensure your code follows a particular code style. Using a consistent code style across your codebase can improve readability. Combining an automatic code formatter with a linter is a great way to improve your code style effortlessly. A very popular code formatter for python is [`black`](https://github.com/psf/black) and will be our tool of choice in this guide.

First, just like the `flake8`, lets add `black` as a development dependency.

```bash
poetry add --dev black
```

!!! note
    We need to configure a few `flake8` settings so that it plays nicely with `black`. Create a `.flake8` file in the top level of your project with the following content.

    ```ini
    [flake8]
    ignore =
        # these rules don't play well with black
        E203  # whitespace before :
        W503  # line break before binary operator
    ```

    Or download it directly from this repository

    ```
    curl -o ./.flake8 https://raw.githubusercontent.com/JohnGiorgi/se_best_practices_ml_perspective/master/.flake8
    ```

Once installed, we can automatically format our code with the following command

```bash
poetry run black .
```

With our code reformatted, lets call the linter again

```
poetry run flake8 .
```

Notice that all the stylistic errors are gone!

With a code formatter and a linter, we can easily and automatically improve our code style, improving consistency and readability within and between our projects. In the next section, we will go over perhaps the most important best practice, testing!