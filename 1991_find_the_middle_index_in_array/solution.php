<?php
// LeetCode 1991 - Find the Middle Index in Array
// https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMiddleIndex($nums) {
        $total = array_sum($nums);
        $left = 0;
        foreach ($nums as $i => $x) {
            if ($left === $total - $left - $x) {
                return $i;
            }
            $left += $x;
        }
        return -1;
    }
}
