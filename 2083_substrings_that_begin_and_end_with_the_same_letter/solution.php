<?php
// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function numberOfSubstrings($s) {
        $freq = array_fill(0, 26, 0);
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
            $ans += $freq[$idx];
        }
        return $ans;
    }
}
