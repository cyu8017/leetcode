<?php
// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function minRemoveToMakeValid($s) {
        $chars = str_split($s);
        $stack = [];
        $n = count($chars);
        for ($i = 0; $i < $n; $i++) {
            if ($chars[$i] === '(') $stack[] = $i;
            elseif ($chars[$i] === ')') {
                if (!empty($stack)) array_pop($stack);
                else $chars[$i] = '';
            }
        }
        foreach ($stack as $i) $chars[$i] = '';
        return implode('', $chars);
    }
}
