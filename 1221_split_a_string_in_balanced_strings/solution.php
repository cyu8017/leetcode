<?php
// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function balancedStringSplit($s) {
        $balance = $answer = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $balance += $s[$i] === 'L' ? 1 : -1;
            if ($balance === 0) $answer++;
        }
        return $answer;
    }
}
