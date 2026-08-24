<?php
// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

class Solution {
    function maximumLength($nums, $k) {
        $n = count($nums);
        $f = [];
        for ($i = 0; $i < $n; $i++) $f[$i] = array_fill(0, $k + 1, 0);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($h = 0; $h <= $k; $h++) {
                for ($j = 0; $j < $i; $j++) {
                    if ($nums[$i] === $nums[$j]) $f[$i][$h] = max($f[$i][$h], $f[$j][$h]);
                    else if ($h > 0) $f[$i][$h] = max($f[$i][$h], $f[$j][$h - 1]);
                }
                $f[$i][$h]++;
            }
            $ans = max($ans, $f[$i][$k]);
        }
        return $ans;
    }
}
