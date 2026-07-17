<?php
// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minProductSum($nums1, $nums2) {
        sort($nums1);
        rsort($nums2);

        $sum = 0;
        $n = count($nums1);
        for ($i = 0; $i < $n; $i++) {
            $sum += $nums1[$i] * $nums2[$i];
        }
        return $sum;
    }
}
