<?php
// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maxFrequency($nums, $k) {
        sort($nums);
        $left = 0;
        $windowSum = 0;
        $best = 0;
        $n = count($nums);

        for ($right = 0; $right < $n; $right++) {
            $value = $nums[$right];
            $windowSum += $value;
            while ($value * ($right - $left + 1) - $windowSum > $k) {
                $windowSum -= $nums[$left];
                $left++;
            }
            $best = max($best, $right - $left + 1);
        }

        return $best;
    }
}
