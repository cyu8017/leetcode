<?php
// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

class Solution {
    function findMinimumTime($tasks) {
        usort($tasks, function($a, $b) { return $a[1] <=> $b[1]; });
        $on = array_fill(0, 2001, false);
        $ans = 0;
        foreach ($tasks as $t) {
            $start = $t[0];
            $end = $t[1];
            $dur = $t[2];
            $have = 0;
            for ($i = $start; $i <= $end; $i++) if ($on[$i]) $have++;
            $need = $dur - $have;
            for ($i = $end; $i >= $start && $need > 0; $i--) {
                if (!$on[$i]) {
                    $on[$i] = true;
                    $need--;
                    $ans++;
                }
            }
        }
        return $ans;
    }
}
