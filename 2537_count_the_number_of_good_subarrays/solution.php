<?php
// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

class Solution {
    function countGood($nums, $k) {
        $freq = [];
        $pairs = 0;
        $ans = 0;
        $left = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $pairs += $freq[$nums[$right]] ?? 0;
            $freq[$nums[$right]] = ($freq[$nums[$right]] ?? 0) + 1;
            while ($pairs >= $k) {
                $ans += $n - $right;
                $freq[$nums[$left]]--;
                $pairs -= $freq[$nums[$left]];
                $left++;
            }
        }
        return $ans;
    }
}
