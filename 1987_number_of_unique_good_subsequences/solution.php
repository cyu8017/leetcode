<?php
// LeetCode 1987 - Number of Unique Good Subsequences
// https://leetcode.com/problems/number-of-unique-good-subsequences/

class Solution {
    /**
     * @param String $binary
     * @return Integer
     */
    function numberOfUniqueGoodSubsequences($binary) {
        $MOD = 1000000007;
        $ends0 = 0;
        $ends1 = 0;
        $has0 = false;
        $n = strlen($binary);
        for ($i = 0; $i < $n; $i++) {
            if ($binary[$i] === '0') {
                $has0 = true;
                $ends0 = ($ends0 + $ends1) % $MOD;
            } else {
                $ends1 = ($ends0 + $ends1 + 1) % $MOD;
            }
        }
        return ($ends0 + $ends1 + ($has0 ? 1 : 0)) % $MOD;
    }
}
