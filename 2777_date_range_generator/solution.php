<?php
// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/

class Solution {
    function dateRangeGenerator($start, $end, $step) {
        $cur = new DateTime($start);
        $last = new DateTime($end);
        $out = [];
        while ($cur <= $last) {
            $out[] = $cur->format('Y-m-d');
            $cur->modify('+' . $step . ' day');
        }
        return $out;
    }
}
