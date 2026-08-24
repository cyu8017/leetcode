<?php
// LeetCode 3290 - Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/

class Solution {
    function maxScore($a, $b) {
        $neg = -1 << 62;
        $dp = [0, $neg, $neg, $neg, $neg];
        foreach ($b as $x) {
            for ($k = 4; $k >= 1; $k--) {
                if ($dp[$k - 1] === $neg) continue;
                $v = $dp[$k - 1] + $a[$k - 1] * $x;
                if ($v > $dp[$k]) $dp[$k] = $v;
            }
        }
        return $dp[4];
    }
}
