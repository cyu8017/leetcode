<?php
// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution {
    function findKthLargest($nums, $k) {
        $target = count($nums) - $k;
        $left = 0;
        $right = count($nums) - 1;
        while ($left <= $right) {
            $pivotIndex = $this->partition($nums, $left, $right);
            if ($pivotIndex === $target) {
                return $nums[$pivotIndex];
            }
            if ($pivotIndex < $target) {
                $left = $pivotIndex + 1;
            } else {
                $right = $pivotIndex - 1;
            }
        }
        return $nums[$left];
    }

    private function partition(&$nums, $left, $right) {
        $pivot = random_int($left, $right);
        [$nums[$pivot], $nums[$right]] = [$nums[$right], $nums[$pivot]];
        $store = $left;
        for ($i = $left; $i < $right; $i++) {
            if ($nums[$i] <= $nums[$right]) {
                [$nums[$store], $nums[$i]] = [$nums[$i], $nums[$store]];
                $store++;
            }
        }
        [$nums[$store], $nums[$right]] = [$nums[$right], $nums[$store]];
        return $store;
    }
}
