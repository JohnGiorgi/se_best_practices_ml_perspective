# Software Engineering Best Practices, a Machine Learners Perspective

This repository is meant to serve as an opinionated, pedagogical guide on software engineering best practices for those of us in machine learning.

__What is this guide NOT?__

It is _NOT_ a comprehensive overview of best practices in software engineering. It is a highly opinionated sampling of tools and ideas that are important for writing good code in a machine learning project. This includes linting, formatting and testing.

__Who is this guide for?__

Machine learners who are not currently following software engineering best practices in their projects but would like to.

__What is machine learning specific about this guide?__

In truth, nothing important. We use `python` as the language of choice as it is popular in machine learning, and we write some machine learning specific tests. Otherwise, this guide could apply to (almost) any python project.

__What tools will this guide cover?__

- [`Poetry`](https://python-poetry.org/docs/#system-requirements), for managing virtual enviornments and package dependencies.
- [`flake8`](https://flake8.pycqa.org/en/latest/), for linting.
- [`black`](https://pypi.org/project/black/), for formatting.
- [`pytest`](https://docs.pytest.org/en/latest/), for testing.
- [GitHub Actions](https://github.com/features/actions), for continous integration / continous development (CI/CD).

## Getting started

To get started, make sure you have Python 3.6 or newer installed.

## Best practice #1: Managing depedencies

Managing depedencies is important for any software project. In machine learning environments, it is particulary important if you care about reproducible results (and you should!).

In Python, the canonical approach is to create isolated _virtual enviroments_ for each of our projects. These virtual enviroments store the specific dependencies needed for a given project, without interferring with the dependencies of _other_ projects (see [here](https://realpython.com/python-virtual-environments-a-primer/) for a great introduction on virtual environments.)

In this guide, we are going to use Poetry, both for creating virtual enviorments and for managing dependencies.