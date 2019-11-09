from unittest.mock import patch 
import unittest
from io import StringIO
import lab4_1 as target 

class TestLab4(unittest.TestCase):
   def test_is_even_true(self):
      user_input = [50]
      with patch('builtins.input', side_effect=user_input):
         resp = target.is_even()
      self.assertIs(resp, True)
   
   def test_is_even_false(self):
      user_input = [51]
      with patch('builtins.input', side_effect=user_input):
         resp = target.is_even()
      self.assertIs(resp, False)
   
   def test_multicondition_is_zero(self):
      user_input = [0]
      expected_output = "Don't be such a zero!"
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.multi_condition()
            output = fake_out.getvalue().strip('\n')
      self.assertEqual(output, expected_output)
   
   def test_multicondition_is_positive_odd(self):
      user_input = [5]
      expected_output = "Positively odd!"
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.multi_condition()
            output = fake_out.getvalue().strip('\n')
      self.assertEqual(output, expected_output)
   
   def test_multicondition_is_even_steven(self):
      user_input = [200004]
      expected_output = "Even Steven!"
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.multi_condition()
            output = fake_out.getvalue().strip('\n')
      self.assertEqual(output, expected_output)

   def test_multicondition_is_negative(self):
      user_input = [-3]
      expected_output = "Negative Nelly!"
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.multi_condition()
            output = fake_out.getvalue().strip('\n')
      self.assertEqual(output, expected_output)
   
   def test_is_underage_21(self):
      user_input = [21]
      expected_output = "You may drink, smoke, and drive if you wish!"
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.is_underage()
            output = fake_out.getvalue().strip('\n')
      self.assertEqual(output, expected_output)

   def test_is_underage_19(self):
      user_input = [19]
      expected_output = "You may smoke and drive!"
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.is_underage()
            output = fake_out.getvalue().strip('\n')
      self.assertEqual(output, expected_output)
   
   def test_is_underage_16(self):
      user_input = [16]
      expected_output = "You may drive!"
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.is_underage()
            output = fake_out.getvalue().strip('\n')
      self.assertEqual(output, expected_output)
   
   def test_is_underage_12(self):
      user_input = [12]
      expected_output = "Enjoy your bike, kid!"
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake_out:
            target.is_underage()
            output = fake_out.getvalue().strip('\n')
      self.assertEqual(output, expected_output)
   
   def test_countdown(self):
      expected_output = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
      with patch('sys.stdout', new = StringIO()) as fake:
         target.countdown()
         output = fake.getvalue().rstrip('\n').split('\n')
      self.assertEqual(output, expected_output)

   def test_guessing_game_q(self):
      user_input = ["q"]
      expected_output = "Goodbye, quitter!"
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake:
            target.guessing_game(6)
            output = fake.getvalue().strip('\n')
      self.assertEqual(output, expected_output)

   def test_guessing_game_win(self):
      user_input = [1, 7, 4]
      expected_output = ["Too Low!", "Too High!", "You win!"]
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake:
            target.guessing_game(4)
            output = fake.getvalue().rstrip('\n').split('\n')
      self.assertEqual(output, expected_output)
   
   def test_guessing_game_lose(self):
      user_input = [0, 10, 1, 9, 2, 8, 3, 7, 4, 6]
      expected_output = [
         "Too Low!",
         "Too High!",
         "Too Low!",
         "Too High!",
         "Too Low!",
         "Too High!",
         "Too Low!",
         "Too High!",
         "Too Low!",
         "Too High!",
         "You Lose!"
      ]
      with patch('builtins.input', side_effect=user_input):
         with patch('sys.stdout', new = StringIO()) as fake:
            target.guessing_game(5)
            output = fake.getvalue().rstrip('\n').split('\n')
      self.assertEqual(output, expected_output)