from i8c.tests import TestCase
import i8c
import sys

class TestEntryPoint(TestCase):
    """Test the console scripts entry point."""

    def setUp(self):
        self.saved_argv = sys.argv
        self.saved_stderr = sys.stderr

    def tearDown(self):
        sys.argv = self.saved_argv
        sys.stderr = self.saved_stderr

    def test_success_path(self):
        """Check the console scripts entry point success path."""
        sys.argv[1:] = ["--version"]
        self.assertIs(i8c.run_compiler(), None)

    def test_failure_path(self):
        """Check the console scripts entry point failure path."""
        sys.argv[1:] = ["-x"]
        sys.stderr = sys.stdout
        self.assertEqual(i8c.run_compiler(), 1)
