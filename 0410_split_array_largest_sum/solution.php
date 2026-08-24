<?php
// LeetCode 0410 - Split Array Largest Sum
// https://leetcode.com/problems/split-array-largest-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function splitArray($nums, $k) {
        return $this->split_array($nums, $k);
    }

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function split_array($nums, $k) {
        $left = max($nums);
        $right = array_sum($nums);

        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($this->canSplit($nums, $k, $mid)) {
                $right = $mid;
            } else {
                $left = $mid + 1;
            }
        }

        return $left;
    }

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $limit
     * @return Boolean
     */
    private function canSplit($nums, $k, $limit) {
        $parts = 1;
        $current = 0;
        foreach ($nums as $value) {
            if ($current + $value > $limit) {
                $parts++;
                $current = 0;
            }
            $current += $value;
        }
        return $parts <= $k;
    }
}
