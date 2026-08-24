<?php
// LeetCode 2466 - Count Ways To Build Good Strings
// https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution {
    function countGoodStrings($low, $high, $zero, $one) {
        $mod = 1000000007;
        $dp = array_fill(0, $high + 1, 0);
        $dp[0] = 1;
        $ans = 0;
        for ($i = 1; $i <= $high; $i++) {
            if ($i >= $zero) $dp[$i] = ($dp[$i] + $dp[$i - $zero]) % $mod;
            if ($i >= $one) $dp[$i] = ($dp[$i] + $dp[$i - $one]) % $mod;
            if ($i >= $low) $ans = ($ans + $dp[$i]) % $mod;
        }
        return $ans;
    }
}
