<?php
// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

class Solution {
    function maximumScore($nums, $k) {
        $n = count($nums);
        $a = array_merge($nums, $nums);
        if ($k > $n) $k = $n;
        $best = 0;
        $NEG = -9007199254740991;
        for ($start = 0; $start < $n; $start++) {
            $seg = array_slice($a, $start, $n);
            $dp = [];
            for ($i = 0; $i <= $n; $i++) $dp[$i] = array_fill(0, $k + 1, $NEG);
            $dp[0][0] = 0;
            for ($i = 1; $i <= $n; $i++) {
                for ($j = 1; $j <= $k && $j <= $i; $j++) {
                    $mx = $NEG;
                    for ($t = $i; $t >= $j; $t--) {
                        if ($seg[$t - 1] > $mx) $mx = $seg[$t - 1];
                        if ($dp[$t - 1][$j - 1] > $NEG) {
                            $cand = $dp[$t - 1][$j - 1] + $mx;
                            if ($cand > $dp[$i][$j]) $dp[$i][$j] = $cand;
                        }
                    }
                }
            }
            if ($dp[$n][$k] > $best) $best = $dp[$n][$k];
        }
        return $best;
    }
}
