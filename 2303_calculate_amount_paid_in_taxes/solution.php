<?php
// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution {
    function calculateTax($brackets, $income) {
        $ans = 0.0;
        $prev = 0;
        foreach ($brackets as $b) {
            $upper = $b[0];
            $percent = $b[1];
            if ($income <= $prev) break;
            $taxable = ($income < $upper) ? $income - $prev : $upper - $prev;
            $ans += $taxable * $percent / 100.0;
            $prev = $upper;
        }
        return $ans;
    }
}
