<?php
// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function maxDepth($s) {
        $depth = $ans = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === "(") {
                $depth++;
                $ans = max($ans, $depth);
            } elseif ($s[$i] === ")") {
                $depth--;
            }
        }
        return $ans;
    }
}
