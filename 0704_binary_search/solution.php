<?php
// LeetCode 0704 - Binary Search
// https://leetcode.com/problems/binary-search/

class Solution {
    function search($nums, $target) {
        $left = 0;
        $right = count($nums) - 1;
        while ($left <= $right) {
            $mid = $left + intdiv($right - $left, 2);
            if ($nums[$mid] === $target) return $mid;
            if ($nums[$mid] < $target) $left = $mid + 1;
            else $right = $mid - 1;
        }
        return -1;
    }
}
