// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> DiffWaysToCompute(string expression) {
        var result = new List<int>();
        if (expression.All(char.IsDigit)) {
            result.Add(int.Parse(expression));
            return result;
        }
        for (int index = 0; index < expression.Length; index++) {
            char operatorChar = expression[index];
            if (operatorChar != '+' && operatorChar != '-' && operatorChar != '*') {
                continue;
            }
            IList<int> left = DiffWaysToCompute(expression[..index]);
            IList<int> right = DiffWaysToCompute(expression[(index + 1)..]);
            foreach (int leftValue in left) {
                foreach (int rightValue in right) {
                    result.Add(operatorChar switch {
                        '+' => leftValue + rightValue,
                        '-' => leftValue - rightValue,
                        _ => leftValue * rightValue,
                    });
                }
            }
        }
        return result;
    }
}
