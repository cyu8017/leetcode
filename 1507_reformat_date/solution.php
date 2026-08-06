<?php
// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/

class Solution {
    /**
     * @param String $date
     * @return String
     */
    function reformatDate($date) {
        $months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
        [$day, $month, $year] = explode(' ', $date);
        $monthNum = array_search($month, $months, true) + 1;
        $dayNum = (int)substr($day, 0, -2);
        return sprintf('%s-%02d-%02d', $year, $monthNum, $dayNum);
    }
}
