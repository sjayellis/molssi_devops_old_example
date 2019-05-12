"""
Unit and regression test for the molssi_devops package.
"""

# Import package, test suite, and other packages as needed
import molssi_devops
import pytest
import sys

def test_molssi_devops_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molssi_devops" in sys.modules
