<?php
// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

class Solution {
    function countPathsWithXorValue($grid, $k) {
        $mod = 1000000007;
        $m = count($grid);
        $n = count($grid[0]);
        $dp = [];
        for ($i = 0; $i < $m; $i++) {
            $dp[$i] = [];
            for ($j = 0; $j < $n; $j++) $dp[$i][$j] = array_fill(0, 16, 0);
        }
        $dp[0][0][$grid[0][0]] = 1;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                for ($x = 0; $x < 16; $x++) {
                    if ($dp[$i][$j][$x] === 0) continue;
                    if ($i + 1 < $m) {
                        $nx = $x ^ $grid[$i + 1][$j];
                        $dp[$i + 1][$j][$nx] = ($dp[$i + 1][$j][$nx] + $dp[$i][$j][$x]) % $mod;
                    }
                    if ($j + 1 < $n) {
                        $nx = $x ^ $grid[$i][$j + 1];
                        $dp[$i][$j + 1][$nx] = ($dp[$i][$j + 1][$nx] + $dp[$i][$j][$x]) % $mod;
                    }
                }
            }
        }
        return $dp[$m - 1][$n - 1][$k];
    }
}
