<?php
// LeetCode 0796 - Rotate String
// https://leetcode.com/problems/rotate-string/

class Solution {
    /**
     * @param String $s
     * @param String $goal
     * @return Boolean
     */
    function rotateString($s, $goal) {
        return strlen($s) === strlen($goal) && strpos($s . $s, $goal) !== false;
    }
}
