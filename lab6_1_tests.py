import unittest
import lab6_1 as target 

class TestLab6(unittest.TestCase):
   def setUp(self):
      self.list_of_words = ["banana", "apple", "grapefruit"]
      self.text = "The banana is greater than the apple. The banana is less than the grapefruit."
      self.file = "test6_1.txt"

   def test_divisible_by_7_true(self):
      self.assertTrue(target.divisible_by_7(49))
      
   def test_divisible_by_7_false(self):
      self.assertFalse(target.divisible_by_7(45))

   def test_compare_it_bad_first_parameter(self):
      self.assertFalse(target.compare_it("string", 5))
   
   def test_compare_it_bad_second_parameter(self):
      self.assertFalse(target.compare_it(5, "string"))
   
   def test_compare_it_not_equal(self):
      self.assertFalse(target.compare_it(5,6))
   
   def test_compare_it_not_positive(self):
      self.assertFalse(target.compare_it(-2, -2))
   
   def test_compare_it_pass(self):
      self.assertTrue(target.compare_it(5, 5))
   
   def test_keyword_counter_boolean_true_works(self):
      expected = {"banana": 2, "apple": 1, "grapefruit": 1}
      out = target.keyword_counter(self.list_of_words, True, self.text)
      self.assertEqual(out, expected)
   
   def test_keyword_counter_reads_file(self):
      expected = {"banana": 6, "apple": 3, "grapefruit": 3}
      out = target.keyword_counter(self.list_of_words, False, self.file)
      self.assertEqual(out, expected)