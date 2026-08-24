<?php
// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer $x
     * @return Integer
     */
    function minOperations($grid, $x) {
        $vals = [];
        $bas = $grid[0][0] % $x;
        foreach ($grid as $row) {
            foreach ($row as $v) {
                if ($v % $x !== $bas) return -1;
                $vals[] = $v;
            }
        }
        sort($vals);
        $median = $vals[intdiv(count($vals), 2)];
        $ans = 0;
        foreach ($vals as $v) $ans += intdiv(abs($v - $median), $x);
        return $ans;
    }
}
