<?php
// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

class Solution {
    function minimumOperations($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $INF = 1 << 29;
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[] = array_fill(0, 10, $INF);
        for ($i = 0; $i < $n; $i++) {
            $cnt = array_fill(0, 10, 0);
            for ($j = 0; $j < $m; $j++) $cnt[$grid[$j][$i]]++;
            if ($i === 0) {
                for ($j = 0; $j < 10; $j++) $f[$i][$j] = $m - $cnt[$j];
            } else {
                for ($j = 0; $j < 10; $j++) {
                    for ($k = 0; $k < 10; $k++) {
                        if ($j !== $k) $f[$i][$j] = min($f[$i][$j], $f[$i - 1][$k] + $m - $cnt[$j]);
                    }
                }
            }
        }
        $ans = $INF;
        for ($j = 0; $j < 10; $j++) $ans = min($ans, $f[$n - 1][$j]);
        return $ans;
    }
}
