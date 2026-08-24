<?php
// LeetCode 0712 - Minimum ASCII Delete Sum for Two Strings
// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution {
    function minimumDeleteSum($s1, $s2) {
        $m = strlen($s1);
        $n = strlen($s2);
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 1; $i <= $m; $i++) $dp[$i][0] = $dp[$i - 1][0] + ord($s1[$i - 1]);
        for ($j = 1; $j <= $n; $j++) $dp[0][$j] = $dp[0][$j - 1] + ord($s2[$j - 1]);
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                if ($s1[$i - 1] === $s2[$j - 1]) $dp[$i][$j] = $dp[$i - 1][$j - 1];
                else $dp[$i][$j] = min($dp[$i - 1][$j] + ord($s1[$i - 1]), $dp[$i][$j - 1] + ord($s2[$j - 1]));
            }
        }
        return $dp[$m][$n];
    }
}
