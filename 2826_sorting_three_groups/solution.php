<?php
// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

class Solution {
    function minimumOperations($nums) {
        $n = count($nums);
        $INF = 1000000000;
        $dp = array_fill(0, $n + 1, array_fill(0, 4, $INF));
        $dp[0][1] = $dp[0][2] = $dp[0][3] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $v = $nums[$i - 1];
            for ($g = 1; $g <= 3; $g++) {
                $cost = $v !== $g ? 1 : 0;
                for ($prev = 1; $prev <= $g; $prev++)
                    $dp[$i][$g] = min($dp[$i][$g], $dp[$i - 1][$prev] + $cost);
            }
        }
        return min($dp[$n][1], $dp[$n][2], $dp[$n][3]);
    }
}
