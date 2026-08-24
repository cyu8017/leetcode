<?php
// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

class Solution {
    function smallestDistancePair($nums, $k) {
        sort($nums);
        $countPairs = function ($distance) use ($nums) {
            $count = 0;
            $left = 0;
            $n = count($nums);
            for ($right = 0; $right < $n; $right++) {
                while ($nums[$right] - $nums[$left] > $distance) $left++;
                $count += $right - $left;
            }
            return $count;
        };
        $lo = 0;
        $hi = $nums[count($nums) - 1] - $nums[0];
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($countPairs($mid) >= $k) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
