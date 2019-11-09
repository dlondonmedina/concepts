from unittest.mock import patch
import unittest 
from io import StringIO
import lab3_1 as target 


class TestLab3(unittest.TestCase):
   def test_sum(self):
      secret = target.sums()
      self.assertEqual(secret, 42)

   def test_name(self):
      correct = ["DYLAN", "dylan", "Dylan", "an"]
      names = target.string_manip("Dylan")
      self.assertEqual(correct, names)

   def test_greeter_bot(self):
      user_input = ["Dylan"]
      expected_output = "Hello, Dylan!"
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.greeter_bot()
            output = fake_out.getvalue().strip("\n")
      self.assertEqual(output, expected_output)

   def test_calculator(self):
      user_input = [32]
      expected_output = 0
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.temp_calculator()
            output = float(fake_out.getvalue().strip())
      self.assertEqual(output, expected_output) 

   def test_bill_splitter(self):
      user_input = [3, 40000, 57000, 88000, 125]
      expected = ["Person 1 should pay $27.03", "Person 2 should pay $38.51", "Person 3 should pay $59.46"]
      output = []
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.equitable_bill_splitter()
            output = fake_out.getvalue().rstrip().split("\n\n")
      
      self.assertEqual(output, expected)

if __name__ == "__main__":
   unittest.main()
