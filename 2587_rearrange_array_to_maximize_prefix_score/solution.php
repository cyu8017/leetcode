<?php
// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

class Solution {
    function maxScore($nums) {
        sort($nums);
        $sum = 0;
        $ans = 0;
        for ($i = count($nums) - 1; $i >= 0; $i--) {
            $sum += $nums[$i];
            if ($sum > 0) $ans++;
            else break;
        }
        return $ans;
    }
}
