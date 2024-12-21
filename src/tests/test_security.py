"""
Tests: test_security
Description: Contains unit tests for the security modules.
"""

from src.security.code_scanner import scan_code

def test_scan_code():
    """Tests the scan_code function."""
    assert scan_code() is True
