<?php
// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

class Solution {
    function minArraySum($nums, $k) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = ($prefix[$i] + $nums[$i]) % $k;
        $inf = PHP_INT_MAX >> 1;
        $dp = array_fill(0, $n + 1, 0);
        $best = array_fill(0, $k, $inf);
        $best[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $dp[$i] = $dp[$i - 1] + $nums[$i - 1];
            if ($best[$prefix[$i]] < $dp[$i]) $dp[$i] = $best[$prefix[$i]];
            if ($dp[$i] < $best[$prefix[$i]]) $best[$prefix[$i]] = $dp[$i];
        }
        return $dp[$n];
    }
}
