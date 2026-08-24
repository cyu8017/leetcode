<?php
// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function firstMissingPositive($nums) {
        $n = count($nums);
        $i = 0;

        while ($i < $n) {
            $value = $nums[$i];
            $target = $value - 1;
            if ($value >= 1 && $value <= $n && $nums[$target] !== $value) {
                $temp = $nums[$i];
                $nums[$i] = $nums[$target];
                $nums[$target] = $temp;
            } else {
                $i++;
            }
        }

        for ($index = 0; $index < $n; $index++) {
            if ($nums[$index] !== $index + 1) {
                return $index + 1;
            }
        }

        return $n + 1;
    }
}
