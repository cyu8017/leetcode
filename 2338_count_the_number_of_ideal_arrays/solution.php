<?php
// LeetCode 2338 - Count the Number of Ideal Arrays
// https://leetcode.com/problems/count-the-number-of-ideal-arrays/

class Solution {
    function idealArrays($n, $maxValue) {
        $mod = 1000000007;
        $maxLen = 14;
        $comb = array_fill(0, $n + 1, array_fill(0, $maxLen + 1, 0));
        for ($i = 0; $i <= $n; $i++) {
            $comb[$i][0] = 1;
            for ($j = 1; $j <= $maxLen && $j <= $i; $j++)
                $comb[$i][$j] = ($comb[$i - 1][$j] + $comb[$i - 1][$j - 1]) % $mod;
        }
        $dp = array_fill(0, $maxValue + 1, array_fill(0, $maxLen + 1, 0));
        for ($i = 1; $i <= $maxValue; $i++) $dp[$i][1] = 1;
        for ($len = 2; $len <= $maxLen; $len++) {
            for ($v = 1; $v <= $maxValue; $v++) {
                for ($m = 2 * $v; $m <= $maxValue; $m += $v)
                    $dp[$m][$len] = ($dp[$m][$len] + $dp[$v][$len - 1]) % $mod;
            }
        }
        $ans = 0;
        for ($v = 1; $v <= $maxValue; $v++) {
            for ($len = 1; $len <= $maxLen && $len <= $n; $len++)
                $ans = ($ans + ($dp[$v][$len] * $comb[$n - 1][$len - 1]) % $mod) % $mod;
        }
        return $ans;
    }
}
