<?php
// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

class Solution {
    function findCoins($numWays) {
        $n = count($numWays);
        $dp = array_fill(0, $n + 1, 0);
        $coins = [];
        $dp[0] = 1;
        for ($amt = 1; $amt <= $n; $amt++) {
            $ways = $numWays[$amt - 1];
            if ($dp[$amt] === $ways) continue;
            if ($dp[$amt] + 1 === $ways) {
                $coins[] = $amt;
                for ($x = $amt; $x <= $n; $x++) $dp[$x] += $dp[$x - $amt];
                if ($dp[$amt] !== $ways) return [];
                continue;
            }
            return [];
        }
        return $coins;
    }
}
