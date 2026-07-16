// LeetCode 0150 - Evaluate Reverse Polish Notation
// https://leetcode.com/problems/evaluate-reverse-polish-notation/

using System;
using System.Collections.Generic;
public class Solution {
    public int EvalRPN(string[] tokens) {
        var stack = new Stack<int>();
        foreach (var token in tokens) {
            if (token is "+" or "-" or "*" or "/") {
                var right = stack.Pop(); var left = stack.Pop();
                stack.Push(token switch { "+" => left + right, "-" => left - right, "*" => left * right, _ => left / right });
            } else stack.Push(int.Parse(token));
        }
        return stack.Pop();
    }
}