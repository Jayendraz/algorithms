from src import Tree
from src import Node

import unittest

class TestExpressionTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()

    def tearDown(self):
        self.tree = None

    def test_should_create_tree_for_valid_mathematical_expression(self):
        # Arrange
        input_string = "(15 / (7 - (1 + 1) ))"

        # Action
        output_tree = self.tree.create_tree(input_string)

        # Assert
        self.assertEqual(output_tree.DataValue, "/")
        self.assertEqual(output_tree.LeftChild.DataValue, "15")
        self.assertEqual(output_tree.RightChild.DataValue, "-")
        self.assertEqual(output_tree.RightChild.LeftChild.DataValue, "7")
        self.assertEqual(output_tree.RightChild.RightChild.DataValue, "+")
        self.assertEqual(output_tree.RightChild.RightChild.LeftChild.DataValue, "1")
        self.assertEqual(output_tree.RightChild.RightChild.RightChild.DataValue, "1")

    def test_should_create_tree_for_valid_mathematical_expression_without_spaces(self):
        # Arrange
        input_string = "(15/(7-(1+1)))"

        # Action
        output_tree = self.tree.create_tree(input_string)

        # Assert
        self.assertEqual(output_tree.DataValue, "/")
        self.assertEqual(output_tree.LeftChild.DataValue, "15")
        self.assertEqual(output_tree.RightChild.DataValue, "-")
        self.assertEqual(output_tree.RightChild.LeftChild.DataValue, "7")
        self.assertEqual(output_tree.RightChild.RightChild.DataValue, "+")
        self.assertEqual(output_tree.RightChild.RightChild.LeftChild.DataValue, "1")
        self.assertEqual(output_tree.RightChild.RightChild.RightChild.DataValue, "1")


    def test_should_not_create_tree_for_empty_mathematical_expression(self):
        # Arrange
        input_string = ""

        # Action & Assert
        self.assertRaises(IndexError, lambda: self.tree.create_tree(input_string))

    def test_should_not_create_tree_for_None_type_mathematical_expression(self):
        # Arrange
        input_string = None

        # Action & Assert
        self.assertRaises(TypeError, lambda: self.tree.create_tree(input_string))

    def test_should_not_create_tree_for_invalid_mathematical_expression_1(self):
        # Arrange
        input_string = "6 +"
        expected_result = "Error!!"

        # Action & Assert
        self.assertRaises(IndexError, lambda: self.tree.create_tree(input_string))

    def test_should_not_create_tree_for_invalid_mathematical_expression_2(self):
        # Arrange
        input_string = "6 + 3 * - 4"
        expected_result = "Error!!"

        # Action & Assert
        self.assertRaises(IndexError, lambda: self.tree.create_tree(input_string))

    def test_should_not_create_tree_for_invalid_mathematical_expression_3(self):
        # Arrange
        input_string = "+ 3 * - 4"
        expected_result = "Error!!"

        # Action & Assert
        self.assertRaises(IndexError, lambda: self.tree.create_tree(input_string))

    def test_should_not_create_tree_for_invalid_mathematical_expression_4(self):
        # Arrange
        input_string = "3 * - 4"
        expected_result = "Error!!"

        # Action & Assert
        self.assertRaises(IndexError, lambda: self.tree.create_tree(input_string))

    def test_should_not_create_tree_for_invalid_mathematical_expression_4(self):
        # Arrange
        input_string = "4 - & + 2"
        expected_result = "Error!!"

        # Action & Assert
        self.assertRaises(KeyError, lambda: self.tree.create_tree(input_string))

    def test_should_not_create_tree_for_invalid_mathematical_expression_5(self):
        # Arrange
        input_string = "A * -B"
        expected_result = "Error!!"

        # Action & Assert
        self.assertRaises(KeyError, lambda: self.tree.create_tree(input_string))

    def test_should_not_create_tree_for_invalid_mathematical_expression_6(self):
        # Arrange
        input_string = "()"
        expected_result = "Error!!"

        # Action & Assert
        self.assertRaises(IndexError, lambda: self.tree.create_tree(input_string))

    def test_valid_mathematical_expression_evaluation(self):
        # Arrange
        input_string = "((15 / (7 - (1 + 1) ) ) * -3 ) - (2 + (1 + 1))"
        expected_result = -13.0

        # Action
        output_tree = self.tree.create_tree(input_string)
        actual_result = self.tree.evaluate(output_tree)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_valid_mathematical_expression_evaluation_all_addition(self):
        # Arrange
        input_string = "((15 + (7 + (1 + 1) ) ) + -3 )"
        expected_result = 21.0

        # Action
        output_tree = self.tree.create_tree(input_string)
        actual_result = self.tree.evaluate(output_tree)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_valid_mathematical_expression_evaluation_all_subtraction(self):
        # Arrange
        input_string = "((15 - (7 - (1 - 1) ) ) - -3 )"
        expected_result = 11

        # Action
        output_tree = self.tree.create_tree(input_string)
        actual_result = self.tree.evaluate(output_tree)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_valid_mathematical_expression_evaluation_all_multiplication(self):
        # Arrange
        input_string = "((15 * (-7 * (1 * -1) ) ) * 3 )"
        expected_result = 315

        # Action
        output_tree = self.tree.create_tree(input_string)
        actual_result = self.tree.evaluate(output_tree)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_valid_mathematical_expression_evaluation_all_division(self):
        # Arrange
        input_string = "((15 / (7 / (1 / 1) ) ) / -3 )"
        expected_result = -0.7142857142857143

        # Action
        output_tree = self.tree.create_tree(input_string)
        actual_result = self.tree.evaluate(output_tree)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_valid_mathematical_expression_evaluation_all_negative_numbers(self):
        # Arrange
        input_string = "((-15 / (-7 - (-1 + -1) ) ) * -3 )"
        expected_result = -9

        # Action
        output_tree = self.tree.create_tree(input_string)
        actual_result = self.tree.evaluate(output_tree)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_valid_mathematical_expression_evaluation_all_3_digits(self):
        # Arrange
        input_string = "((150 / (-105 / (-236 + 179) ) ) * 373 )"
        expected_result = 30372.857142857145

        # Action
        output_tree = self.tree.create_tree(input_string)
        actual_result = self.tree.evaluate(output_tree)

        # Assert
        self.assertEqual(expected_result, actual_result)
