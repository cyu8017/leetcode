// LeetCode 0032 - Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function longestValidParentheses($s) {
        $stack = [-1];
        $best = 0;
        $n = strlen($s);

        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '(') {
                $stack[] = $i;
            } else {
                array_pop($stack);
                if (empty($stack)) {
                    $stack[] = $i;
                } else {
                    $best = max($best, $i - $stack[count($stack) - 1]);
                }
            }
        }

        return $best;
    }
}
