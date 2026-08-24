<?php
// LeetCode 0035 - Search Insert Position
// https://leetcode.com/problems/search-insert-position/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function searchInsert($nums, $target) {
        $left = 0;
        $right = count($nums);

        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($nums[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }

        return $left;
    }
}
