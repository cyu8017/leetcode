<?php
// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

class Solution {
    function rangeSum($nums) {
        $mod = 1000000007;
        $cnt = [];
        $sum = [];
        $ans = 0;
        foreach ($nums as $x) {
            $cL = $cnt[$x - 1] ?? 0;
            $sL = $sum[$x - 1] ?? 0;
            $cR = $cnt[$x + 1] ?? 0;
            $sR = $sum[$x + 1] ?? 0;
            $c = (1 + $cL + $cR) % $mod;
            $s = ($x + $sL + ($cL * $x % $mod) + $sR + ($cR * $x % $mod)) % $mod;
            if ($cL > 0 && $cR > 0) {
                $c = ($c + ($cL * $cR % $mod)) % $mod;
                $s = ($s + ($sL * $cR % $mod) + ($sR * $cL % $mod) + ($cL * $cR % $mod * $x % $mod)) % $mod;
            }
            $cnt[$x] = (($cnt[$x] ?? 0) + $c) % $mod;
            $sum[$x] = (($sum[$x] ?? 0) + $s) % $mod;
            $ans = ($ans + $s) % $mod;
        }
        return $ans;
    }
}
