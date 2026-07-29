<?php
// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

class Solution {
    /**
     * @param Integer[][] $costs
     * @return Integer
     */
    function twoCitySchedCost($costs) {
        usort($costs, function ($a, $b) {
            return ($a[0] - $a[1]) - ($b[0] - $b[1]);
        });
        $n = intdiv(count($costs), 2);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans += $costs[$i][0];
        }
        for ($i = $n; $i < 2 * $n; $i++) {
            $ans += $costs[$i][1];
        }
        return $ans;
    }
}
