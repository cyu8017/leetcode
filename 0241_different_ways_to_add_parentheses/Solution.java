// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        List<Integer> result = new ArrayList<>();
        if (expression.chars().allMatch(Character::isDigit)) {
            result.add(Integer.parseInt(expression));
            return result;
        }
        for (int index = 0; index < expression.length(); index++) {
            char operator = expression.charAt(index);
            if (operator != '+' && operator != '-' && operator != '*') {
                continue;
            }
            List<Integer> left = diffWaysToCompute(expression.substring(0, index));
            List<Integer> right = diffWaysToCompute(expression.substring(index + 1));
            for (int leftValue : left) {
                for (int rightValue : right) {
                    if (operator == '+') {
                        result.add(leftValue + rightValue);
                    } else if (operator == '-') {
                        result.add(leftValue - rightValue);
                    } else {
                        result.add(leftValue * rightValue);
                    }
                }
            }
        }
        return result;
    }
}
