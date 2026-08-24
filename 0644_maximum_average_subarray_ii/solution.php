<?php
// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

class Solution {
    function findMaxAverage($nums, $k) {
        $canReach = function($mid) use ($nums, $k) {
            $prefix = 0;
            for ($i = 0; $i < $k; ++$i) $prefix += $nums[$i] - $mid;
            if ($prefix >= 0) return true;
            $prev = 0;
            $minPrev = 0;
            for ($i = $k; $i < count($nums); ++$i) {
                $prefix += $nums[$i] - $mid;
                $prev += $nums[$i - $k] - $mid;
                $minPrev = min($minPrev, $prev);
                if ($prefix - $minPrev >= 0) return true;
            }
            return false;
        };
        $left = min($nums);
        $right = max($nums);
        for ($i = 0; $i < 80; ++$i) {
            $mid = ($left + $right) / 2;
            if ($canReach($mid)) $left = $mid;
            else $right = $mid;
        }
        return $left;
    }
}
