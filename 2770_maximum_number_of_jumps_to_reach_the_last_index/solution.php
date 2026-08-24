<?php
// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

class Solution {
    function maximumJumps($nums, $target) {
        $n = count($nums);
        $dp = array_fill(0, $n, -1);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] < 0) continue;
            for ($j = $i + 1; $j < $n; $j++) {
                if (abs($nums[$j] - $nums[$i]) <= $target)
                    $dp[$j] = max($dp[$j], $dp[$i] + 1);
            }
        }
        return $dp[$n - 1];
    }
}
