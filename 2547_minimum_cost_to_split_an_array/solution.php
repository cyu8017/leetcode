<?php
// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

class Solution {
    function minCost($nums, $k) {
        $n = count($nums);
        $INF = intdiv(PHP_INT_MAX, 2);
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            $freq = [];
            $trimmed = 0;
            for ($j = $i; $j < $n; $j++) {
                $c = ($freq[$nums[$j]] ?? 0) + 1;
                $freq[$nums[$j]] = $c;
                if ($c === 2) $trimmed += 2;
                else if ($c > 2) $trimmed++;
                $cost = $dp[$i] + $k + $trimmed;
                if ($cost < $dp[$j + 1]) $dp[$j + 1] = $cost;
            }
        }
        return $dp[$n];
    }
}
