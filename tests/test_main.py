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
