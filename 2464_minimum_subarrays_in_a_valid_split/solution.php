<?php
// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

class Solution {
    function validSubarraySplit($nums) {
        $gcd = function ($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $n = count($nums);
        $INF = 1 << 30;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] >= $INF) continue;
            for ($j = $i; $j < $n; $j++) {
                if ($gcd($nums[$i], $nums[$j]) > 1) {
                    if ($dp[$i] + 1 < $dp[$j + 1]) $dp[$j + 1] = $dp[$i] + 1;
                }
            }
        }
        return $dp[$n] >= $INF ? -1 : $dp[$n];
    }
}
