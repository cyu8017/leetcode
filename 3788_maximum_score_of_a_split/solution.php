<?php
// LeetCode 3788 - Maximum Score of a Split
// https://leetcode.com/problems/maximum-score-of-a-split/

class Solution {
    function maximumScore($nums) {
        $n = count($nums);
        $suf = array_fill(0, $n, 0);
        $suf[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $suf[$i] = min($nums[$i], $suf[$i + 1]);
        $pre = 0;
        $ans = -9007199254740991;
        for ($i = 0; $i < $n - 1; $i++) {
            $pre += $nums[$i];
            $ans = max($ans, $pre - $suf[$i + 1]);
        }
        return $ans;
    }
}
