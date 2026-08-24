<?php
// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution {
    function minGroups($intervals) {
        $events = [];
        foreach ($intervals as $it) {
            $events[] = [$it[0], 1];
            $events[] = [$it[1] + 1, -1];
        }
        usort($events, function($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] - $b[0];
            return $a[1] - $b[1];
        });
        $cur = 0;
        $ans = 0;
        foreach ($events as $e) {
            $cur += $e[1];
            $ans = max($ans, $cur);
        }
        return $ans;
    }
}
