<?php
// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

class Solution {
    function lateFee($daysLate) {
        $fee = function($x) {
            if ($x === 1) return 1;
            if ($x > 5) return 3 * $x;
            return 2 * $x;
        };
        $ans = 0;
        foreach ($daysLate as $x) $ans += $fee($x);
        return $ans;
    }
}
