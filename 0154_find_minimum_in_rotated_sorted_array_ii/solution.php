<?php
// LeetCode 0154 - Find Minimum in Rotated Sorted Array II
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution {
    function findMin(array $nums): int {
        $left = 0;
        $right = count($nums) - 1;
        while ($left < $right) {
            $middle = intdiv($left + $right, 2);
            if ($nums[$middle] > $nums[$right]) {
                $left = $middle + 1;
            } elseif ($nums[$middle] < $nums[$right]) {
                $right = $middle;
            } else {
                $right--;
            }
        }
        return $nums[$left];
    }
}
