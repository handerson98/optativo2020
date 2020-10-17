from Project import createApp
import unittest, sys

app = createApp()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('Project', pattern='test_*.py')

    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        sys.exit(0)
    sys.exit(1)
