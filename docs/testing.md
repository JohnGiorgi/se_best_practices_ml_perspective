This is the most important section in the guide. Unit tests are short tests that assert the output of some function or method equals the expected value for some given input. They allow us to ensure our code does what we think it does, reducing bugs and making it dramatically easier to refactor our code down the line.

There are multiple unit testing frameworks in Python, but we will use a very popular one, [`pytest`](https://docs.pytest.org/en/latest/).

Typically, tests are grouped under a `tests` directory (Poetry created this for us automatically). Let's start by creating a file, `test_main.py` under `tests`.

```bash
touch tests/test_main.py
```

As is common, we will group our tests for a class under another class, like so

```python
from se_best_practices_ml_perspective.main import LitClassifier


class TestLitClassifier:
    def test_forward(self):
        assert False

    def test_training_step(self):
        assert False

    def test_validation_step(self):
        assert False

    def test_configure_optimizers(self):
        assert False
```

We start with one unit test per method of `LitClassifier`. A passing test must contain an `assert` statement that evaluates to `True`. To run our unit tests, we simply call

```
poetry run pytest
```

Notice that all four tests fail, as expected.

```bash
================================================== short test summary info ==================================================
FAILED tests/test_main.py::TestLitClassifier::test_forward - assert False
FAILED tests/test_main.py::TestLitClassifier::test_training_step - assert False
FAILED tests/test_main.py::TestLitClassifier::test_validation_step - assert False
FAILED tests/test_main.py::TestLitClassifier::test_configure_optimizers - assert False
```

Let's get each test to pass, one-by-one, starting with `test_forward`.

``` python hl_lines="9 10 11 12 13 14 15"
from se_best_practices_ml_perspective.main import LitClassifier
import torch


class TestLitClassifier:
    model = LitClassifier()

    def test_forward(self):
        """Assert that the output shape of `LitClassifier.forward` is as expected."""
        inputs = torch.randn(1, 28, 28)
        outputs = self.model.forward(inputs)

        expected_size = (1, 10)
        actual_size = outputs.size()
        assert actual_size == expected_size

    def test_training_step(self):
        assert False

    def test_validation_step(self):
        assert False

    def test_configure_optimizers(self):
        assert False
```

Here, we add a simple test that asserts for some random input, the output is of the expected shape. Running the tests again, we will notice that `test_forward` is now passing.

```
================================================== short test summary info ==================================================
FAILED tests/test_main.py::TestLitClassifier::test_training_step - assert False
FAILED tests/test_main.py::TestLitClassifier::test_validation_step - assert False
FAILED tests/test_main.py::TestLitClassifier::test_configure_optimizers - assert False
```

Continuing with the remaining tests


``` python hl_lines="18 19 20 21 22 25 26 27 28 29 32 33 34 35 36 37"
from se_best_practices_ml_perspective.main import LitClassifier
import torch


class TestLitClassifier:
    model = LitClassifier()

    def test_forward(self):
        """Assert that the output shape of `LitClassifier.forward` is as expected."""
        inputs = torch.randn(1, 28, 28)
        outputs = self.model.forward(inputs)

        expected_size = (1, 10)
        actual_size = outputs.size()
        assert actual_size == expected_size

    def test_training_step(self):
        """Assert that `LitClassifier.training_step` returns a non-empty dictionary."""
        inputs = (torch.randn(1, 28, 28), torch.randint(10, (1,)))
        results = self.model.training_step(batch=inputs, batch_idx=0)
        assert isinstance(results, dict)
        assert results

    def test_validation_step(self):
        """Assert that `LitClassifier.validation_step` returns a non-empty dictionary."""
        inputs = (torch.randn(1, 28, 28), torch.randint(10, (1,)))
        results = self.model.validation_step(batch=inputs, batch_idx=0)
        assert isinstance(results, dict)
        assert results

    def test_configure_optimizers(self):
        """Assert that `LitClassifier.configure_optimizers` returns an Adam optimizer with the
        expected learning rate.
        """
        optimizer = self.model.configure_optimizers()
        assert isinstance(optimizer, torch.optim.Adam)
        assert optimizer.param_groups[0]["lr"] == 0.02
```

In this quick overview of unit testing, we wrote simple tests for each method of our neural network classifier. We then checked that all tests are passing, increasing our confidence that our code works as expected. In the future, if we were to refactor our code, we could re-run our tests to ensure we didn't break anything.

In the next and final section, we will see how to tie everything we have learned together and automate the process of linting, formatting and testing.