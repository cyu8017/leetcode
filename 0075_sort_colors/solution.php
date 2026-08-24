<?php
// LeetCode 0075 - Sort Colors
// https://leetcode.com/problems/sort-colors/

class Solution {
    /**
     * @param Integer[] $nums
     * @return void
     */
    function sortColors(&$nums) {
        $low = 0;
        $mid = 0;
        $high = count($nums) - 1;

        while ($mid <= $high) {
            if ($nums[$mid] === 0) {
                $tmp = $nums[$low];
                $nums[$low] = $nums[$mid];
                $nums[$mid] = $tmp;
                $low++;
                $mid++;
            } elseif ($nums[$mid] === 1) {
                $mid++;
            } else {
                $tmp = $nums[$mid];
                $nums[$mid] = $nums[$high];
                $nums[$high] = $tmp;
                $high--;
            }
        }
    }
}
