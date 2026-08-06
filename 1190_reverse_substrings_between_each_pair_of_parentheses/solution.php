<?php
// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function reverseParentheses($s) {
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch === ')') {
                $chunk = [];
                while (!empty($stack) && end($stack) !== '(') $chunk[] = array_pop($stack);
                array_pop($stack);
                foreach ($chunk as $c) $stack[] = $c;
            } else {
                $stack[] = $ch;
            }
        }
        return implode('', $stack);
    }
}
