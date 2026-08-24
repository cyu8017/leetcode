<?php
// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution {
    function countWays($ranges) {
        $MOD = 1000000007;
        usort($ranges, function($a, $b) { return $a[0] <=> $b[0]; });
        $groups = 0;
        $end = -1;
        foreach ($ranges as $r) {
            if ($r[0] > $end) {
                $groups++;
                $end = $r[1];
            } else if ($r[1] > $end) {
                $end = $r[1];
            }
        }
        $ans = 1;
        for ($i = 0; $i < $groups; $i++) $ans = $ans * 2 % $MOD;
        return $ans;
    }
}
