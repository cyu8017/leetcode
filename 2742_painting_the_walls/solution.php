<?php
// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

class Solution {
    function paintWalls($cost, $time) {
        $n = count($cost);
        $INF = 1000000000000;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $n; $j >= 0; $j--) {
                $nj = min($n, $j + $time[$i] + 1);
                if ($dp[$j] + $cost[$i] < $dp[$nj]) $dp[$nj] = $dp[$j] + $cost[$i];
            }
        }
        return $dp[$n];
    }
}
