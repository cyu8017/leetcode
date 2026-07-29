<?php
// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function removeOuterParentheses($s) {
        $ans = '';
        $depth = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch === '(') {
                if ($depth > 0) {
                    $ans .= $ch;
                }
                $depth++;
            } else {
                $depth--;
                if ($depth > 0) {
                    $ans .= $ch;
                }
            }
        }
        return $ans;
    }
}
