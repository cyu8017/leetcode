<?php
// LeetCode 1004 - Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function longestOnes($nums, $k) {
        $left = $zeros = $ans = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $zeros += $nums[$right] === 0 ? 1 : 0;
            while ($zeros > $k) {
                $zeros -= $nums[$left] === 0 ? 1 : 0;
                $left++;
            }
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
