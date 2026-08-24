<?php
// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

class Solution {
    function numberOfSubsequences($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 2; $j < $n; $j++) {
                for ($k = $j + 2; $k < $n; $k++) {
                    for ($l = $k + 2; $l < $n; $l++) {
                        if ($nums[$i] * $nums[$k] === $nums[$j] * $nums[$l]) $ans++;
                    }
                }
            }
        }
        return $ans;
    }
}
