<?php
// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minOperations($nums1, $nums2) {
        if (count($nums1) * 6 < count($nums2) || count($nums2) * 6 < count($nums1)) {
            return -1;
        }
        $s1 = array_sum($nums1);
        $s2 = array_sum($nums2);
        if ($s1 === $s2) {
            return 0;
        }
        if ($s1 < $s2) {
            [$nums1, $nums2] = [$nums2, $nums1];
            [$s1, $s2] = [$s2, $s1];
        }
        $diff = $s1 - $s2;
        $gains = [];
        foreach ($nums1 as $x) {
            $gains[] = $x - 1;
        }
        foreach ($nums2 as $x) {
            $gains[] = 6 - $x;
        }
        rsort($gains);
        $ops = 0;
        foreach ($gains as $gain) {
            if ($diff <= 0) {
                break;
            }
            $diff -= $gain;
            $ops++;
        }
        return $diff <= 0 ? $ops : -1;
    }
}
