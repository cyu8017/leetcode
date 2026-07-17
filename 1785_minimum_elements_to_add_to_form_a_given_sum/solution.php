<?php
// LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
// https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $limit
     * @param Integer $goal
     * @return Integer
     */
    function minElements($nums, $limit, $goal) {
        $diff = abs(array_sum($nums) - $goal);
        return intdiv($diff + $limit - 1, $limit);
    }
}
