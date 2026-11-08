"""作者：Wangyuan；日期：2026-11-08。职责：通过合成输入复验已确认缺陷。"""
import unittest
from unittest.mock import patch
import registry
from core import run
class ReleaseTests(unittest.TestCase):
 def test_request_data_not_saved_to_global(self) -> None:
  original=registry.TOOLS
  with patch('registry._load_registry',side_effect=AssertionError('global data read')):
   self.assertEqual(run({'tools':[{'kind':'web'}]})['tool_count'],1)
  self.assertIs(registry.TOOLS,original)
