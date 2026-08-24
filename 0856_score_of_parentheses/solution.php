<?php
// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function scoreOfParentheses($s) {
        $stack = [0];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '(') $stack[] = 0;
            else {
                $val = array_pop($stack);
                $stack[] = array_pop($stack) + max(2 * $val, 1);
            }
        }
        return $stack[count($stack) - 1];
    }
}
