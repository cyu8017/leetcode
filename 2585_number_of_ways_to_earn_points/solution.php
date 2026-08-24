<?php
// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

class Solution {
    function waysToReachTarget($target, $types) {
        $MOD = 1000000007;
        $dp = array_fill(0, $target + 1, 0);
        $dp[0] = 1;
        foreach ($types as $t) {
            $count = $t[0];
            $marks = $t[1];
            for ($s = $target; $s >= 0; $s--) {
                for ($k = 1; $k <= $count && $s - $k * $marks >= 0; $k++) {
                    $dp[$s] = ($dp[$s] + $dp[$s - $k * $marks]) % $MOD;
                }
            }
        }
        return $dp[$target];
    }
}
