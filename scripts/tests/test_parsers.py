#!/usr/bin/env python3
"""Unit tests for parser and config helpers."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))

from example_parser import parse_example_text  # noqa: E402
from metadata_parser import parse_python3_snippet  # noqa: E402
from pandas_parser import parse_pandas_examples_from_markdown  # noqa: E402
from sql_shell_parser import parse_sql_examples_from_markdown  # noqa: E402
from test_config import build_config  # noqa: E402


class ExampleParserTests(unittest.TestCase):
    def test_two_sum_example(self) -> None:
        text = (
            "Input: nums = [2,7,11,15], target = 9\n"
            "Output: [0,1]\n"
            "Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."
        )
        parsed = parse_example_text(text)
        self.assertIsNotNone(parsed)
        assert parsed is not None
        self.assertEqual(parsed["args"]["nums"], [2, 7, 11, 15])
        self.assertEqual(parsed["args"]["target"], 9)
        self.assertEqual(parsed["expected"], [0, 1])

    def test_scalar_output(self) -> None:
        text = "Input: x = 5\nOutput: 10"
        parsed = parse_example_text(text)
        self.assertIsNotNone(parsed)
        assert parsed is not None
        self.assertEqual(parsed["args"]["x"], 5)
        self.assertEqual(parsed["expected"], 10)

    def test_design_prelude_lines(self) -> None:
        text = (
            "Input:\n1\n1\n"
            '["BoundedBlockingQueue","enqueue"]\n'
            "[[2],[1]]\n"
            "Output: [1]\n"
        )
        parsed = parse_example_text(text)
        self.assertIsNotNone(parsed)
        assert parsed is not None
        self.assertEqual(parsed["kind"], "design")
        self.assertEqual(parsed["operations"][0], "BoundedBlockingQueue")

    def test_pandas_colon_assignment(self) -> None:
        md = (
            "## Problem\n\n"
            "Write a solution to create a DataFrame.\n\n"
            "**Example 1:**\n\n"
            "```\n"
            "**Input:\n"
            "**student_data:**\n"
            "**[\n"
            "  [1, 15],\n"
            "  [2, 11]\n"
            "]\n"
            "**Output:**\n"
            "+------------+-----+\n"
            "| student_id | age |\n"
            "+------------+-----+\n"
            "| 1          | 15  |\n"
            "| 2          | 11  |\n"
            "+------------+-----+\n"
            "```\n"
        )
        cases = parse_pandas_examples_from_markdown(md)
        self.assertEqual(len(cases), 1)
        self.assertEqual(cases[0]["kind"], "pandas")
        self.assertEqual(cases[0]["args"]["student_data"], [[1, 15], [2, 11]])

    def test_sql_bare_table_names(self) -> None:
        md = (
            "## Problem\n\n"
            "Table: `Visits`\n\n"
            "**Example 1:**\n\n"
            "```\n"
            "**Input:**\n"
            "Visits\n"
            "+----------+-------------+\n"
            "| visit_id | customer_id |\n"
            "+----------+-------------+\n"
            "| 1        | 23          |\n"
            "+----------+-------------+\n"
            "**Output:**\n"
            "+-------------+\n"
            "| customer_id |\n"
            "+-------------+\n"
            "| 23          |\n"
            "+-------------+\n"
            "```\n"
        )
        cases = parse_sql_examples_from_markdown(md)
        self.assertEqual(len(cases), 1)
        self.assertEqual(cases[0]["kind"], "sql")
        self.assertEqual(cases[0]["tables"]["Visits"][0]["customer_id"], 23)


class MetadataParserTests(unittest.TestCase):
    def test_python_snippet(self) -> None:
        code = (
            "class Solution:\n"
            "    def twoSum(self, nums: List[int], target: int) -> List[int]:\n"
            "        pass\n"
        )
        parsed = parse_python3_snippet(code)
        self.assertIsNotNone(parsed)
        assert parsed is not None
        self.assertEqual(parsed["class"], "Solution")
        self.assertEqual(parsed["method"], "twoSum")
        self.assertEqual(parsed["paramOrder"], ["nums", "target"])


    def test_operations_input_is_not_design(self) -> None:
        text = (
            "Input: nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]\n"
            "Output: [3,2,7,1]"
        )
        parsed = parse_example_text(text)
        self.assertIsNotNone(parsed)
        assert parsed is not None
        self.assertNotIn("kind", parsed)
        self.assertIn("args", parsed)
        self.assertEqual(parsed["expected"], [3, 2, 7, 1])
    def test_design_config(self) -> None:
        cases = [
            {
                "kind": "design",
                "operations": ["WordDistance", "shortest"],
                "arguments": [[["a", "b"], ["a", "b"]], ["a", "b"]],
                "expected": [None, 1],
            }
        ]
        config = build_config({}, None, cases)
        self.assertEqual(config["kind"], "design")
        self.assertEqual(config["class"], "WordDistance")
        self.assertNotIn("method", config)

    def test_sql_config_marks_not_runnable(self) -> None:
        cases = [{"kind": "sql", "tables": {"T": []}, "expected": []}]
        config = build_config({}, None, cases)
        self.assertEqual(config["kind"], "sql")
        self.assertFalse(config["runnable"])

    def test_pandas_config_marks_not_runnable(self) -> None:
        cases = [{"kind": "pandas", "args": {"student_data": []}, "expected": []}]
        metadata = {"method": "createDataframe", "paramOrder": ["student_data"]}
        config = build_config({}, metadata, cases)
        self.assertEqual(config["kind"], "pandas")
        self.assertEqual(config["method"], "createDataframe")
        self.assertFalse(config["runnable"])


if __name__ == "__main__":
    unittest.main()
