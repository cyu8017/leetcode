<?php
// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution {
    function numSubarraysWithSum($nums, $goal) {
        $atMost = function ($g) use ($nums) {
            if ($g < 0) return 0;
            $left = 0;
            $sum = 0;
            $ans = 0;
            $n = count($nums);
            for ($right = 0; $right < $n; $right++) {
                $sum += $nums[$right];
                while ($sum > $g) $sum -= $nums[$left++];
                $ans += $right - $left + 1;
            }
            return $ans;
        };
        return $atMost($goal) - $atMost($goal - 1);
    }
}
