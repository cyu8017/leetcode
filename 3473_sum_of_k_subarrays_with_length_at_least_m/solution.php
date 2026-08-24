<?php
// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

class Solution {
    function maxSum($nums, $k, $m) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $neg = intdiv(PHP_INT_MIN, 4);
        $dp = [];
        for ($t = 0; $t <= $k; $t++) $dp[$t] = array_fill(0, $n + 1, $neg);
        for ($i = 0; $i <= $n; $i++) $dp[0][$i] = 0;
        for ($t = 1; $t <= $k; $t++) {
            $best = $neg;
            for ($i = $t * $m; $i <= $n; $i++) {
                $j = $i - $m;
                $best = max($best, $dp[$t - 1][$j] - $pref[$j]);
                $dp[$t][$i] = $best + $pref[$i];
            }
            for ($i = 1; $i <= $n; $i++) $dp[$t][$i] = max($dp[$t][$i], $dp[$t][$i - 1]);
        }
        return $dp[$k][$n];
    }
}
