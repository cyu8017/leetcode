<?php
// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

class Solution {
    function minAbsDiff($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = [];
        for ($i = 0; $i <= $m - $k; $i++) $ans[$i] = array_fill(0, $n - $k + 1, 0);
        for ($i = 0; $i <= $m - $k; $i++) {
            for ($j = 0; $j <= $n - $k; $j++) {
                $nums = [];
                for ($x = $i; $x < $i + $k; $x++)
                    for ($y = $j; $y < $j + $k; $y++) $nums[] = $grid[$x][$y];
                sort($nums);
                $d = 2147483647;
                for ($t = 1; $t < count($nums); $t++) {
                    if ($nums[$t] !== $nums[$t - 1]) $d = min($d, abs($nums[$t] - $nums[$t - 1]));
                }
                if ($d !== 2147483647) $ans[$i][$j] = $d;
            }
        }
        return $ans;
    }
}
