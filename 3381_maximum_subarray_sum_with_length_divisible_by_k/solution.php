<?php
// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

class Solution {
    function maxSubarraySum($nums, $k) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $INF = PHP_INT_MAX;
        $best = array_fill(0, $k, $INF);
        $best[0] = 0;
        $ans = PHP_INT_MIN;
        for ($i = 1; $i <= $n; $i++) {
            $r = $i % $k;
            if ($best[$r] !== $INF) {
                $cand = $pref[$i] - $best[$r];
                if ($cand > $ans) $ans = $cand;
            }
            if ($pref[$i] < $best[$r]) $best[$r] = $pref[$i];
        }
        return $ans;
    }
}
