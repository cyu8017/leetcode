<?php
// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

class Solution {
    function maxTurbulenceSize($arr) {
        $ans = 1;
        $cur = 1;
        $n = count($arr);
        for ($i = 1; $i < $n; $i++) {
            if ($arr[$i] === $arr[$i - 1]) $cur = 1;
            elseif ($i === 1 || ($arr[$i] - $arr[$i - 1]) * ($arr[$i - 1] - $arr[$i - 2]) < 0) $cur++;
            else $cur = 2;
            $ans = max($ans, $cur);
        }
        return $ans;
    }
}
