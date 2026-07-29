<?php
// LeetCode 1003 - Check If Word Is Valid After Substitutions
// https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $stack[] = $s[$i];
            $len = count($stack);
            if ($len >= 3 && $stack[$len - 3] === 'a' && $stack[$len - 2] === 'b' && $stack[$len - 1] === 'c') {
                array_pop($stack);
                array_pop($stack);
                array_pop($stack);
            }
        }
        return count($stack) === 0;
    }
}
