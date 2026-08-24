<?php
// LeetCode 0162 - Find Peak Element
// https://leetcode.com/problems/find-peak-element/

class Solution {
    function findPeakElement(array $nums): int {
        $left = 0;
        $right = count($nums) - 1;
        while ($left < $right) {
            $mid = $left + intdiv($right - $left, 2);
            if ($nums[$mid] > $nums[$mid + 1]) $right = $mid;
            else $left = $mid + 1;
        }
        return $left;
    }
}
