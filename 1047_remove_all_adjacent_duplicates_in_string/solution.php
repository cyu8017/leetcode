<?php
// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function removeDuplicates($s) {
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (!empty($stack) && $stack[count($stack) - 1] === $ch) {
                array_pop($stack);
            } else {
                $stack[] = $ch;
            }
        }
        return implode('', $stack);
    }
}
