<?php
// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function movesToMakeZigzag($nums) {
        $cost = function ($start) use ($nums) {
            $ans = 0;
            $n = count($nums);
            for ($i = $start; $i < $n; $i += 2) {
                $left = $i > 0 ? $nums[$i - 1] : PHP_INT_MAX;
                $right = $i + 1 < $n ? $nums[$i + 1] : PHP_INT_MAX;
                $ans += max(0, $nums[$i] - min($left, $right) + 1);
            }
            return $ans;
        };
        return min($cost(0), $cost(1));
    }
}
