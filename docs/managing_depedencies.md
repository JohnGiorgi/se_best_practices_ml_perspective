Managing dependencies is important for any software project. In machine learning environments, it is particularly important if you care about reproducible results (and you should!).

In Python, the canonical approach is to create isolated _virtual enviroments_ for each of our projects. These virtual environments store the specific dependencies needed for a given project, without interfering with the dependencies of _other_ projects.

!!! note
    See [here](https://realpython.com/python-virtual-environments-a-primer/) for a great introduction to virtual environments.

In this guide, we are going to use Poetry, both for creating virtual environments and for managing dependencies.

## Installing Poetry

To install poetry, run one of the following commands, depending on your system.

=== "osx / linux / bash on windows"

    ```bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
    ```

=== "windows powershell"

    ```powershell
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
    ```

## Creating a Python Package with Poetry

With Poetry installed, we can create our first project like so

```bash
poetry new se_best_practices_ml_perspective
```

!!! note
    The remainder of the guide will assume you have called it `se_best_practices_ml_perspective`, but you can name it whatever you want.

Notice that poetry has automatically created a project directory for us. This includes a `README`, a main package directory `se_best_practices_ml_perspective`, and a `tests` directory (we will return to this later).

```bash
se_best_practices_ml_perspective
├── README.rst
├── pyproject.toml
├── se_best_practices_ml_perspective
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_se_best_practices_ml_perspective.py
```

Most importantly, `pyproject.toml` is the configuration file (automatically generated by Poetry) that will contain metadata about our package (like its name, version, and a description) along with our dependencies. Besides the `authors` line highlighted in yellow, your `pyproject.toml` should look like the following.

``` toml hl_lines="5"
[tool.poetry]
name = "se_best_practices_ml_perspective"
version = "0.1.0"
description = ""
authors = ["johngiorgi <johnmgiorgi@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.7"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```

## Adding Dependencies with Poetry

Adding dependencies is easy. Simply call `poetry add <package_name>`. For example, we will need `pytorch-lightning` and `torchvision` in this guide.

```
poetry add pytorch-lightning torchvision
```

Poetry will _automatically_ create a virtual environment if one does not exist, and add `pytorch-lightning` and `torchvision` as dependencies to `pyproject.toml`.

``` toml hl_lines="9 10"
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

[build-system]
requires = ["poetry>=0.12"]
```

That's it for now. In the next section, we will go over linting and formatting.