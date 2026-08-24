<?php
// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

class Solution {
    function modPow($a, $e, $mod) {
        $r = 1;
        $a %= $mod;
        while ($e > 0) {
            if ($e & 1) $r = $r * $a % $mod;
            $a = $a * $a % $mod;
            $e >>= 1;
        }
        return $r;
    }

    function numberOfWays($n, $x, $y) {
        $mod = 1000000007;
        $dp = [];
        for ($i = 0; $i <= $n; $i++) $dp[$i] = array_fill(0, $x + 1, 0);
        $dp[0][0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            for ($j = 1; $j <= $x && $j <= $i; $j++) {
                $dp[$i][$j] = ($dp[$i - 1][$j - 1] + $j * $dp[$i - 1][$j] % $mod) % $mod;
            }
        }
        $fact = [1];
        for ($i = 1; $i <= $x; $i++) $fact[$i] = $fact[$i - 1] * $i % $mod;
        $ans = 0;
        $ypow = 1;
        for ($k = 1; $k <= $x && $k <= $n; $k++) {
            $ypow = $ypow * $y % $mod;
            $perm = $fact[$x] * $this->modPow($fact[$x - $k], $mod - 2, $mod) % $mod;
            $ans = ($ans + $dp[$n][$k] * $perm % $mod * $ypow % $mod) % $mod;
        }
        return $ans;
    }
}
