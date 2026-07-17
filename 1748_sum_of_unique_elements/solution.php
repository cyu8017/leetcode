<?php
// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfUnique($nums) {
        $counts = array_count_values($nums);
        $total = 0;
        foreach ($counts as $value => $count) {
            if ($count === 1) {
                $total += $value;
            }
        }
        return $total;
    }
}
