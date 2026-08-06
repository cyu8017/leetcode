<?php
// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class Solution {
    /**
     * @param Integer[][] $logs
     * @param Integer $n
     * @return Integer
     */
    function earliestAcq($logs, $n) {
        $parent = range(0, $n - 1);
        $find = function ($x) use (&$parent, &$find) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        usort($logs, fn($a, $b) => $a[0] <=> $b[0]);
        $components = $n;
        foreach ($logs as $log) {
            [$t, $a, $b] = $log;
            $ra = $find($a);
            $rb = $find($b);
            if ($ra === $rb) continue;
            $parent[$rb] = $ra;
            $components--;
            if ($components === 1) return $t;
        }
        return -1;
    }
}
