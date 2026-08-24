<?php
// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

class Solution {
    function maximumPossibleSize($nums) {
        $ans = 0;
        $mx = 0;
        foreach ($nums as $x) {
            if ($mx <= $x) {
                $ans++;
                $mx = $x;
            }
        }
        return $ans;
    }
}
