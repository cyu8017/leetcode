<?php
// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

class Solution {
    function maxCoins($lane1, $lane2) {
        $n = count($lane1);
        $neg = intdiv(PHP_INT_MIN, 4);
        $dp = [[$lane1[0], $neg], [$lane2[0], $neg]];
        $ans = max($dp[0][0], $dp[1][0]);
        for ($i = 1; $i < $n; $i++) {
            $ndp = [[0, 0], [0, 0]];
            $ndp[0][0] = max($dp[0][0], 0) + $lane1[$i];
            $ndp[1][0] = max($dp[1][0], 0) + $lane2[$i];
            $ndp[0][1] = max($dp[0][1], $dp[1][0]) + $lane1[$i];
            $ndp[1][1] = max($dp[1][1], $dp[0][0]) + $lane2[$i];
            if ($lane1[$i] > $ndp[0][0]) $ndp[0][0] = $lane1[$i];
            if ($lane2[$i] > $ndp[1][0]) $ndp[1][0] = $lane2[$i];
            for ($a = 0; $a < 2; $a++)
                for ($b = 0; $b < 2; $b++) {
                    $dp[$a][$b] = $ndp[$a][$b];
                    if ($dp[$a][$b] > $ans) $ans = $dp[$a][$b];
                }
        }
        return $ans;
    }
}
