<?php
// LeetCode 3183 - The Number of Ways to Make the Sum
// https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

class Solution {
    function numberOfWays($n) {
        $mod = 1000000007;
        $coins = [1, 2, 6];
        $f = array_fill(0, $n + 1, 0);
        $f[0] = 1;
        foreach ($coins as $x) {
            for ($j = $x; $j <= $n; $j++) $f[$j] = ($f[$j] + $f[$j - $x]) % $mod;
        }
        $ans = $f[$n];
        if ($n >= 4) $ans = ($ans + $f[$n - 4]) % $mod;
        if ($n >= 8) $ans = ($ans + $f[$n - 8]) % $mod;
        return $ans;
    }
}
