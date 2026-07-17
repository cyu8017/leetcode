<?php
// LeetCode 1716 - Calculate Money in Leetcode Bank
// https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function totalMoney($n) {
        $weeks = intdiv($n, 7);
        $days = $n % 7;
        return $weeks * 28 + intdiv(7 * $weeks * ($weeks - 1), 2) + $days * ($weeks + 1) + intdiv($days * ($days - 1), 2);
    }
}
