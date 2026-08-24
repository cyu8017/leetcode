<?php
// LeetCode 2132 - Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer $stampHeight
     * @param Integer $stampWidth
     * @return Boolean
     */
    function possibleToStamp($grid, $stampHeight, $stampWidth) {
        $m = count($grid);
        $n = count($grid[0]);
        $pref = [];
        for ($i = 0; $i <= $m; $i++) $pref[$i] = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                $pref[$i + 1][$j + 1] = $pref[$i + 1][$j] + $pref[$i][$j + 1] - $pref[$i][$j] + $grid[$i][$j];
        $diff = [];
        for ($i = 0; $i <= $m; $i++) $diff[$i] = array_fill(0, $n + 1, 0);
        for ($i = 0; $i + $stampHeight - 1 < $m; $i++) {
            for ($j = 0; $j + $stampWidth - 1 < $n; $j++) {
                $sum = $pref[$i + $stampHeight][$j + $stampWidth] - $pref[$i][$j + $stampWidth]
                    - $pref[$i + $stampHeight][$j] + $pref[$i][$j];
                if ($sum === 0) {
                    $diff[$i][$j]++;
                    $diff[$i][$j + $stampWidth]--;
                    $diff[$i + $stampHeight][$j]--;
                    $diff[$i + $stampHeight][$j + $stampWidth]++;
                }
            }
        }
        $cur = [];
        for ($i = 0; $i < $m; $i++) $cur[$i] = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $v = $diff[$i][$j];
                if ($i > 0) $v += $cur[$i - 1][$j];
                if ($j > 0) $v += $cur[$i][$j - 1];
                if ($i > 0 && $j > 0) $v -= $cur[$i - 1][$j - 1];
                $cur[$i][$j] = $v;
                if ($grid[$i][$j] === 0 && $v === 0) return false;
            }
        }
        return true;
    }
}
