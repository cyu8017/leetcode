<?php
// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution {
    function minimumEffort($tasks) {
        usort($tasks, function($a, $b) {
            return ($b[1] - $b[0]) - ($a[1] - $a[0]);
        });
        $energy = 0;
        $spent = 0;
        foreach ($tasks as [$cost, $minimum]) {
            $energy = max($energy, $spent + $minimum);
            $spent += $cost;
        }
        return $energy;
    }
}
