<?php
// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

class Solution {
    function minimumWhiteTiles($floor, $numCarpets, $carpetLen) {
        $n = strlen($floor);
        $INF = 1 << 30;
        $dp = [];
        for ($c = 0; $c <= $numCarpets; $c++) $dp[$c] = array_fill(0, $n + 1, $INF);
        $dp[0][0] = 0;
        for ($j = 1; $j <= $n; $j++)
            $dp[0][$j] = $dp[0][$j - 1] + ($floor[$j - 1] === '1' ? 1 : 0);
        for ($c = 1; $c <= $numCarpets; $c++) {
            $dp[$c][0] = 0;
            for ($j = 1; $j <= $n; $j++) {
                $dp[$c][$j] = $dp[$c][$j - 1] + ($floor[$j - 1] === '1' ? 1 : 0);
                $start = max(0, $j - $carpetLen);
                $dp[$c][$j] = min($dp[$c][$j], $dp[$c - 1][$start]);
            }
        }
        return $dp[$numCarpets][$n];
    }
}
