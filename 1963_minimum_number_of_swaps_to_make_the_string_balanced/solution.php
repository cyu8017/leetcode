<?php
// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minSwaps($s) {
        $bal = 0;
        $mx = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '[') {
                $bal++;
            } else {
                $bal--;
            }
            $mx = min($mx, $bal);
        }
        return intdiv(-$mx + 1, 2);
    }
}
