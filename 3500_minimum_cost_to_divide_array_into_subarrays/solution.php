<?php
// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

class Solution {
    function minimumCost($nums, $cost, $k) {
        $n = count($nums);
        $pn = array_fill(0, $n + 1, 0);
        $pc = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pn[$i + 1] = $pn[$i] + $nums[$i];
            $pc[$i + 1] = $pc[$i] + $cost[$i];
        }
        $inf = intdiv(PHP_INT_MAX, 4);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $dp[$i] = $inf;
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $i; $j < $n; $j++) {
                $cand = $pn[$j + 1] * ($pc[$j + 1] - $pc[$i]) + $k * ($pc[$n] - $pc[$i]) + $dp[$j + 1];
                if ($cand < $dp[$i]) $dp[$i] = $cand;
            }
        }
        return $dp[0];
    }
}
