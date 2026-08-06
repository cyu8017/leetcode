<?php
// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

class Solution {
    /**
     * @param String $date
     * @return Integer
     */
    function dayOfYear($date) {
        [$year, $month, $day] = array_map('intval', explode('-', $date));
        $leap = ($year % 4 === 0 && $year % 100 !== 0) || ($year % 400 === 0);
        $days = [31, $leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        return array_sum(array_slice($days, 0, $month - 1)) + $day;
    }
}
