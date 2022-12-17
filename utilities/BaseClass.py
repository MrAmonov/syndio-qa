import pytest

# This file is to use the class for the test cases that will be run using the parameters
# We could also implement logging within this BaseClass below if required


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass
