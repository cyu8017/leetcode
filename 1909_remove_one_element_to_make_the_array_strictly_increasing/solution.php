<?php
// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution {
    function canBeIncreasing($nums) {
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] <= $nums[$i - 1]) {
                return $this->check($nums, $i - 1) || $this->check($nums, $i);
            }
        }
        return true;
    }

    private function check($nums, $skip) {
        $prev = null;
        foreach ($nums as $i => $x) {
            if ($i === $skip) {
                continue;
            }
            if ($prev !== null && $x <= $prev) {
                return false;
            }
            $prev = $x;
        }
        return true;
    }
}
