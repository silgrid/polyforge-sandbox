# carries: greet.py, test_greet.py, .polyforge/verify-scope.conf, .polyforge/Dockerfile.verify
import subprocess
import sys
import unittest
from pathlib import Path

from greet import greet


class GreetTest(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("polyforge"), "Hello, polyforge!")


class GreetingNormalizationTest(unittest.TestCase):
    def test_function_normalization(self):
        cases = [
            ("  polyforge  ", "Hello, polyforge!"),
            ("", "Hello, world!"),
            (" \t\n", "Hello, world!"),
            ("Ada Lovelace", "Hello, Ada Lovelace!"),
            ("  Ada  Lovelace  ", "Hello, Ada  Lovelace!"),
            ("\u2003Ada\u2003", "Hello, Ada!"),
            ("  Ada\tLovelace  ", "Hello, Ada\tLovelace!"),
        ]
        for name, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(greet(name), expected)

    def test_cli_normalization(self):
        script = Path(__file__).with_name("greet.py")
        cases = [
            ([], "Hello, world!\n"),
            (["  polyforge  "], "Hello, polyforge!\n"),
            ([""], "Hello, world!\n"),
            ([" \t\n"], "Hello, world!\n"),
        ]
        for arguments, expected in cases:
            with self.subTest(arguments=arguments):
                result = subprocess.run(
                    [sys.executable, str(script), *arguments],
                    capture_output=True,
                    text=True,
                    timeout=10,
                    check=False,
                )
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stderr, "")
                self.assertEqual(result.stdout, expected)


if __name__ == "__main__":
    unittest.main()
