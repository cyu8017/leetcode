<?php
// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

class Solution {
    function sumOfPower($nums) {
        $MOD = 1000000007;
        sort($nums);
        $ans = 0;
        $s = 0;
        foreach ($nums as $x) {
            $ans = ($ans + (($s + $x) % $MOD) * $x % $MOD * $x) % $MOD;
            $s = ($s * 2 + $x) % $MOD;
        }
        return $ans;
    }
}
