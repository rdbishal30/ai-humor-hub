import unittest
import subprocess
import sys
from funny_drawing import generate_funny_drawing

class TestFunnyDrawing(unittest.TestCase):

    def test_generate_funny_drawing_returns_string(self):
        """Tests that generate_funny_drawing returns a non-empty string."""
        drawing = generate_funny_drawing()
        self.assertIsInstance(drawing, str)
        self.assertTrue(len(drawing) > 0)

    def test_script_runs_successfully(self):
        """Tests that the script runs without errors and prints output."""
        process = subprocess.Popen(
            [sys.executable, "funny_drawing.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()

        self.assertEqual(process.returncode, 0, f"Script exited with error:\n{stderr}")
        self.assertTrue(len(stdout) > 0, "Script produced no output.")

if __name__ == "__main__":
    unittest.main()
