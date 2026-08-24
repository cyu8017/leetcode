<?php
// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

class Solution {
    function maximumAmount($coins) {
        $m = count($coins);
        $n = count($coins[0]);
        $neg = -(1 << 30);
        $dp = [];
        for ($i = 0; $i < $m; $i++) {
            $dp[$i] = [];
            for ($j = 0; $j < $n; $j++) $dp[$i][$j] = array_fill(0, 3, $neg);
        }
        if ($coins[0][0] < 0) {
            $dp[0][0][0] = $coins[0][0];
            $dp[0][0][1] = 0;
            $dp[0][0][2] = 0;
        } else {
            $dp[0][0][0] = $coins[0][0];
            $dp[0][0][1] = $coins[0][0];
            $dp[0][0][2] = $coins[0][0];
        }
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i === 0 && $j === 0) continue;
                for ($k = 0; $k < 3; $k++) {
                    $best = $neg;
                    if ($i > 0) $best = max($best, $dp[$i - 1][$j][$k]);
                    if ($j > 0) $best = max($best, $dp[$i][$j - 1][$k]);
                    if ($best === $neg) continue;
                    if ($coins[$i][$j] >= 0) $dp[$i][$j][$k] = $best + $coins[$i][$j];
                    else $dp[$i][$j][$k] = max($dp[$i][$j][$k], $best + $coins[$i][$j]);
                }
                for ($k = 1; $k < 3; $k++) {
                    $best = $neg;
                    if ($i > 0) $best = max($best, $dp[$i - 1][$j][$k - 1]);
                    if ($j > 0) $best = max($best, $dp[$i][$j - 1][$k - 1]);
                    if ($best !== $neg && $coins[$i][$j] < 0)
                        $dp[$i][$j][$k] = max($dp[$i][$j][$k], $best);
                }
            }
        }
        return max($dp[$m - 1][$n - 1][0], max($dp[$m - 1][$n - 1][1], $dp[$m - 1][$n - 1][2]));
    }
}
