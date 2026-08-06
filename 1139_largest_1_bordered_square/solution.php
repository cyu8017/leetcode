<?php
// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largest1BorderedSquare($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $hor = array_fill(0, $m, array_fill(0, $n, 0));
        $ver = array_fill(0, $m, array_fill(0, $n, 0));
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 0) continue;
                $hor[$i][$j] = ($j > 0 ? $hor[$i][$j - 1] : 0) + 1;
                $ver[$i][$j] = ($i > 0 ? $ver[$i - 1][$j] : 0) + 1;
            }
        }
        for ($len = min($m, $n); $len >= 1; $len--) {
            for ($i = $len - 1; $i < $m; $i++) {
                for ($j = $len - 1; $j < $n; $j++) {
                    if ($hor[$i][$j] >= $len && $ver[$i][$j] >= $len
                        && $hor[$i - $len + 1][$j] >= $len
                        && $ver[$i][$j - $len + 1] >= $len) {
                        return $len * $len;
                    }
                }
            }
        }
        return 0;
    }
}
