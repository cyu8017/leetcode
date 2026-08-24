<?php
// LeetCode 0829 - Consecutive Numbers Sum
// https://leetcode.com/problems/consecutive-numbers-sum/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function consecutiveNumbersSum($n) {
        $ans = 0;
        for ($k = 1; $k * ($k - 1) / 2 < $n; $k++) {
            if (($n - intdiv($k * ($k - 1), 2)) % $k === 0) $ans++;
        }
        return $ans;
    }
}
