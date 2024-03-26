MARKER = """\
integration: mark a test as a unit test
high: High Priority
medium: Medium Priority
low: Low Priority
"""


def pytest_configure(config):
    for line in MARKER.strip().split("\n"):
        config.addinivalue_line("markers", line)
