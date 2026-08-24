<?php
// LeetCode 3247 - Number of Subsequences with Odd Sum
// https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

class Solution {
    function subsequenceCount($nums) {
        $mod = 1000000007;
        $f = [0, 0];
        foreach ($nums as $x) {
            $g = [0, 0];
            if ($x % 2 === 1) {
                $g[0] = ($f[0] + $f[1]) % $mod;
                $g[1] = ($f[0] + $f[1] + 1) % $mod;
            } else {
                $g[0] = ($f[0] + $f[0] + 1) % $mod;
                $g[1] = ($f[1] + $f[1]) % $mod;
            }
            $f = $g;
        }
        return $f[1];
    }
}
