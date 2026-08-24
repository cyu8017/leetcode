<?php
// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minSwap($nums1, $nums2) {
        $n = count($nums1);
        $swap = array_fill(0, $n, $n);
        $keep = array_fill(0, $n, $n);
        $swap[0] = 1;
        $keep[0] = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($nums1[$i] > $nums1[$i - 1] && $nums2[$i] > $nums2[$i - 1]) {
                $keep[$i] = $keep[$i - 1];
                $swap[$i] = $swap[$i - 1] + 1;
            }
            if ($nums1[$i] > $nums2[$i - 1] && $nums2[$i] > $nums1[$i - 1]) {
                $keep[$i] = min($keep[$i], $swap[$i - 1]);
                $swap[$i] = min($swap[$i], $keep[$i - 1] + 1);
            }
        }
        return min($swap[$n - 1], $keep[$n - 1]);
    }
}
