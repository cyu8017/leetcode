<?php
// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function validSubarrays($nums) {
        $stack = [];
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            while (!empty($stack) && $nums[end($stack)] > $nums[$i]) {
                $j = array_pop($stack);
                $ans += $i - $j;
            }
            $stack[] = $i;
        }
        while (!empty($stack)) {
            $j = array_pop($stack);
            $ans += $n - $j;
        }
        return $ans;
    }
}
