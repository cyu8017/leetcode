<?php
// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

class Solution {
    function fixedRatio($s, $num1, $num2) {
        $pref = [];
        $pref[0] = 1;
        $zeros = 0;
        $ones = 0;
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') $zeros++;
            else $ones++;
            $key = $zeros * $num2 - $ones * $num1;
            $ans += isset($pref[$key]) ? $pref[$key] : 0;
            if (!isset($pref[$key])) $pref[$key] = 0;
            $pref[$key]++;
        }
        return $ans;
    }
}
