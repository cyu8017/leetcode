<?php
// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function kthSmallestSubarraySum($nums, $k) {
        $lo = min($nums);
        $hi = array_sum($nums);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->count($nums, $mid) >= $k) {
                $hi = $mid;
            } else {
                $lo = $mid + 1;
            }
        }
        return $lo;
    }

    private function count($nums, $limit) {
        $total = 0;
        $left = 0;
        $ans = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $total += $nums[$right];
            while ($total > $limit) {
                $total -= $nums[$left];
                $left++;
            }
            $ans += $right - $left + 1;
        }
        return $ans;
    }
}
