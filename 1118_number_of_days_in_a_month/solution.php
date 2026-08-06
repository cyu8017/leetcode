<?php
// LeetCode 1118 - Number of Days in a Month
// https://leetcode.com/problems/number-of-days-in-a-month/

class Solution {
    /**
     * @param Integer $year
     * @param Integer $month
     * @return Integer
     */
    function numberOfDays($year, $month) {
        $days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        if ($month !== 2) return $days[$month];
        $leap = ($year % 4 === 0 && $year % 100 !== 0) || ($year % 400 === 0);
        return $leap ? 29 : 28;
    }
}
