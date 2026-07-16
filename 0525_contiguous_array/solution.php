<?php
// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaxLength($nums) {
        return $this->find_max_length($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function find_max_length($nums) {
        $counts = [0 => -1];
        $balance = 0;
        $best = 0;
        foreach ($nums as $index => $num) {
            $balance += $num === 1 ? 1 : -1;
            if (array_key_exists($balance, $counts)) {
                $best = max($best, $index - $counts[$balance]);
            } else {
                $counts[$balance] = $index;
            }
        }
        return $best;
    }
}
