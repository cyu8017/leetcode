<?php
// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

class Solution {
    function minMaxSums($nums, $k) {
        $mod = 1000000007;
        sort($nums);
        $n = count($nums);
        $C = [];
        for ($i = 0; $i <= $n; $i++) $C[$i] = array_fill(0, $k, 0);
        for ($i = 0; $i <= $n; $i++) {
            $C[$i][0] = 1;
            for ($j = 1; $j < $k && $j <= $i; $j++) $C[$i][$j] = ($C[$i - 1][$j] + $C[$i - 1][$j - 1]) % $mod;
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $waysMax = 0;
            for ($j = 0; $j < $k && $j <= $i; $j++) $waysMax = ($waysMax + $C[$i][$j]) % $mod;
            $waysMin = 0;
            $right = $n - $i - 1;
            for ($j = 0; $j < $k && $j <= $right; $j++) $waysMin = ($waysMin + $C[$right][$j]) % $mod;
            $ans = ($ans + $nums[$i] * $waysMax % $mod + $nums[$i] * $waysMin % $mod) % $mod;
        }
        return $ans;
    }
}
