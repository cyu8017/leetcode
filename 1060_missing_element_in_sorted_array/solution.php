<?php
// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function missingElement($nums, $k) {
        $missing = function ($i) use ($nums) {
            return $nums[$i] - $nums[0] - $i;
        };
        $n = count($nums);
        if ($k > $missing($n - 1)) {
            return $nums[$n - 1] + $k - $missing($n - 1);
        }
        $lo = 0;
        $hi = $n - 1;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($missing($mid) < $k) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        return $nums[$lo - 1] + $k - $missing($lo - 1);
    }
}
