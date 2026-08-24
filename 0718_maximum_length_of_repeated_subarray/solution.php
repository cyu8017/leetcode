<?php
// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution {
    function findLength($nums1, $nums2) {
        $m = count($nums1);
        $n = count($nums2);
        $best = 0;
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $m; $i++) {
            $next = array_fill(0, $n + 1, 0);
            for ($j = 1; $j <= $n; $j++) {
                if ($nums1[$i - 1] === $nums2[$j - 1]) {
                    $next[$j] = $dp[$j - 1] + 1;
                    $best = max($best, $next[$j]);
                }
            }
            $dp = $next;
        }
        return $best;
    }
}
