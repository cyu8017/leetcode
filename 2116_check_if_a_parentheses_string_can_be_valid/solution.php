<?php
// LeetCode 2116 - Check if a Parentheses String Can Be Valid
// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution {
    /**
     * @param String $s
     * @param String $locked
     * @return Boolean
     */
    function canBeValid($s, $locked) {
        $n = strlen($s);
        if ($n % 2 !== 0) return false;
        $bal = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($locked[$i] === '0' || $s[$i] === '(') $bal++;
            else $bal--;
            if ($bal < 0) return false;
        }
        $bal = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($locked[$i] === '0' || $s[$i] === ')') $bal++;
            else $bal--;
            if ($bal < 0) return false;
        }
        return true;
    }
}
