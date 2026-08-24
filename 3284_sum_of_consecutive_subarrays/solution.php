<?php
// LeetCode 3284 - Sum of Consecutive Subarrays
// https://leetcode.com/problems/sum-of-consecutive-subarrays/

class Solution {
    function rangeSum($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $ans = 0;
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j + 1 < $n && ($nums[$j + 1] === $nums[$j] + 1 || $nums[$j + 1] === $nums[$j] - 1)) $j++;
            for ($L = $i; $L <= $j; $L++) {
                $s = 0;
                for ($R = $L; $R <= $j; $R++) {
                    $s += $nums[$R];
                    $ans = ($ans + $s) % $mod;
                }
            }
            $i = $j + 1;
        }
        return $ans;
    }
}
