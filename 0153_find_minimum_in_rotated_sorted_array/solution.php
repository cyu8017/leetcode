<?php
// LeetCode 0153 - Find Minimum in Rotated Sorted Array
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution {
    function findMin(array $nums): int {
        $left = 0;
        $right = count($nums) - 1;
        while ($left < $right) {
            $middle = intdiv($left + $right, 2);
            if ($nums[$middle] > $nums[$right]) {
                $left = $middle + 1;
            } else {
                $right = $middle;
            }
        }
        return $nums[$left];
    }
}
