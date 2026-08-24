<?php
// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution {
    /**
     * @param int[] $nums
     * @return int[]
     */
    function findDisappearedNumbers($nums) {
        return $this->find_disappeared_numbers($nums);
    }

    /**
     * @param int[] $nums
     * @return int[]
     */
    function find_disappeared_numbers($nums) {
        foreach ($nums as $number) {
            $index = abs($number) - 1;
            if ($nums[$index] > 0) {
                $nums[$index] = -$nums[$index];
            }
        }
        $result = [];
        foreach ($nums as $index => $value) {
            if ($value > 0) {
                $result[] = $index + 1;
            }
        }
        return $result;
    }
}
