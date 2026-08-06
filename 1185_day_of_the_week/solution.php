<?php
// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

class Solution {
    /**
     * @param Integer $day
     * @param Integer $month
     * @param Integer $year
     * @return String
     */
    function dayOfTheWeek($day, $month, $year) {
        return date('l', strtotime(sprintf('%04d-%02d-%02d', $year, $month, $day)));
    }
}
