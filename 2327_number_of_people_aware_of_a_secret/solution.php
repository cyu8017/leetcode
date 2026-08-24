<?php
// LeetCode 2327 - Number of People Aware of a Secret
// https://leetcode.com/problems/number-of-people-aware-of-a-secret/

class Solution {
    function peopleAwareOfSecret($n, $delay, $forget) {
        $mod = 1000000007;
        $dp = array_fill(0, $n + 1, 0);
        $dp[1] = 1;
        $share = 0;
        for ($day = 2; $day <= $n; ++$day) {
            if ($day - $delay >= 1) $share = ($share + $dp[$day - $delay]) % $mod;
            if ($day - $forget >= 1) $share = ($share - $dp[$day - $forget] + $mod) % $mod;
            $dp[$day] = $share;
        }
        $ans = 0;
        for ($day = $n - $forget + 1; $day <= $n; ++$day)
            if ($day >= 1) $ans = ($ans + $dp[$day]) % $mod;
        return $ans;
    }
}
