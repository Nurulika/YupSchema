# test_yupschema.py
"""
Tests for YupSchema module.
"""

import unittest
from yupschema import YupSchema

class TestYupSchema(unittest.TestCase):
    """Test cases for YupSchema class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = YupSchema()
        self.assertIsInstance(instance, YupSchema)
        
    def test_run_method(self):
        """Test the run method."""
        instance = YupSchema()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
