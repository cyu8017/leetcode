<?php
// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer[][]
     */
    function shiftGrid($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $flat = [];
        foreach ($grid as $row) foreach ($row as $v) $flat[] = $v;
        $len = count($flat);
        $k %= $len;
        if ($k) $flat = array_merge(array_slice($flat, -$k), array_slice($flat, 0, $len - $k));
        $ans = [];
        for ($i = 0; $i < $m; $i++) $ans[] = array_slice($flat, $i * $n, $n);
        return $ans;
    }
}
