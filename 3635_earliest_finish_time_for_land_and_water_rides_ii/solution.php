<?php
// LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

class Solution {
    function earliestFinishTime($landStartTime, $landDuration, $waterStartTime, $waterDuration) {
        $calc = function($a1, $t1, $a2, $t2) {
            $minEnd = PHP_INT_MAX;
            $n1 = count($a1);
            for ($i = 0; $i < $n1; $i++) $minEnd = min($minEnd, $a1[$i] + $t1[$i]);
            $ans = PHP_INT_MAX;
            $n2 = count($a2);
            for ($i = 0; $i < $n2; $i++) $ans = min($ans, max($minEnd, $a2[$i]) + $t2[$i]);
            return $ans;
        };
        return min(
            $calc($landStartTime, $landDuration, $waterStartTime, $waterDuration),
            $calc($waterStartTime, $waterDuration, $landStartTime, $landDuration)
        );
    }
}
