<?php
// LeetCode 0414 - Third Maximum Number
// https://leetcode.com/problems/third-maximum-number/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function thirdMax($nums) {
        return $this->third_max($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function third_max($nums) {
        $first = $second = $third = null;

        foreach ($nums as $value) {
            if ($value === $first || $value === $second || $value === $third) {
                continue;
            }
            if ($first === null || $value > $first) {
                $third = $second;
                $second = $first;
                $first = $value;
            } elseif ($second === null || $value > $second) {
                $third = $second;
                $second = $value;
            } elseif ($third === null || $value > $third) {
                $third = $value;
            }
        }

        return $third !== null ? $third : $first;
    }
}
