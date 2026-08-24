<?php
// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

class Solution {
    function specialTriplets($nums) {
        $left = [];
        $right = [];
        foreach ($nums as $x) $right[$x] = ($right[$x] ?? 0) + 1;
        $ans = 0;
        $mod = 1000000007;
        foreach ($nums as $x) {
            $right[$x] = $right[$x] - 1;
            $lv = $left[$x * 2] ?? 0;
            $rv = $right[$x * 2] ?? 0;
            $ans = ($ans + $lv * $rv % $mod) % $mod;
            $left[$x] = ($left[$x] ?? 0) + 1;
        }
        return $ans;
    }
}
