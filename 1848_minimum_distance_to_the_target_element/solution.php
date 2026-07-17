<?php
// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @param Integer $start
     * @return Integer
     */
    function getMinDistance($nums, $target, $start) {
        $best = count($nums);
        foreach ($nums as $i => $value) {
            if ($value === $target) {
                $best = min($best, abs($i - $start));
            }
        }
        return $best;
    }
}
