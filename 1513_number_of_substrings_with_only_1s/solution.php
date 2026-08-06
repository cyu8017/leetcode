<?php
// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function numSub($s) {
        $ans = 0;
        $run = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $run = $s[$i] === '1' ? $run + 1 : 0;
            $ans += $run;
        }
        return $ans % 1000000007;
    }
}
