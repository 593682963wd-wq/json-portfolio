import unittest,tempfile,json
from pathlib import Path
from core import run

class Tests(unittest.TestCase):
 def test_stats(self):self.assertEqual(run(json.loads(Path('example.json').read_text()))['tool_count'],2)
 def test_empty(self):self.assertEqual(run({})['tool_count'],0)
 def test_bad(self):
  with self.assertRaises(ValueError):run({'tools':[3]})
 def test_page(self):
  from app import app
  self.assertEqual(app.test_client().get('/').status_code,200)

if __name__=="__main__":unittest.main()
