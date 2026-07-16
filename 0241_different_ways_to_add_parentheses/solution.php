// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution {
    /**
     * @param String $expression
     * @return Integer[]
     */
    function diffWaysToCompute($expression) {
        if (ctype_digit($expression)) {
            return [(int) $expression];
        }
        $result = [];
        $length = strlen($expression);
        for ($index = 0; $index < $length; $index++) {
            $operator = $expression[$index];
            if ($operator !== '+' && $operator !== '-' && $operator !== '*') {
                continue;
            }
            $left = $this->diffWaysToCompute(substr($expression, 0, $index));
            $right = $this->diffWaysToCompute(substr($expression, $index + 1));
            foreach ($left as $leftValue) {
                foreach ($right as $rightValue) {
                    if ($operator === '+') {
                        $result[] = $leftValue + $rightValue;
                    } elseif ($operator === '-') {
                        $result[] = $leftValue - $rightValue;
                    } else {
                        $result[] = $leftValue * $rightValue;
                    }
                }
            }
        }
        return $result;
    }
}
