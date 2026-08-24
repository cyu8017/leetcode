<?php
// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

class Solution {
    function sumOfGoodSubsequences($nums) {
        $mod = 1000000007;
        $cnt = [];
        $sum = [];
        $ans = 0;
        foreach ($nums as $x) {
            $c = 1;
            $s = $x;
            if (($cnt[$x - 1] ?? 0) > 0) {
                $c = ($c + $cnt[$x - 1]) % $mod;
                $s = ($s + $sum[$x - 1] + $cnt[$x - 1] * $x % $mod) % $mod;
            }
            if (($cnt[$x + 1] ?? 0) > 0) {
                $c = ($c + $cnt[$x + 1]) % $mod;
                $s = ($s + $sum[$x + 1] + $cnt[$x + 1] * $x % $mod) % $mod;
            }
            $cnt[$x] = (($cnt[$x] ?? 0) + $c) % $mod;
            $sum[$x] = (($sum[$x] ?? 0) + $s) % $mod;
            $ans = ($ans + $s) % $mod;
        }
        return $ans;
    }
}
