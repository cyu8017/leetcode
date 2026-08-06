<?php
// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function rangeSum($nums, $n, $left, $right) {
        $values = [];
        for ($i = 0; $i < $n; $i++) {
            $total = 0;
            for ($j = $i; $j < $n; $j++) {
                $total += $nums[$j];
                $values[] = $total;
            }
        }
        sort($values);
        $sum = 0;
        for ($i = $left - 1; $i < $right; $i++) {
            $sum += $values[$i];
        }
        return $sum % 1000000007;
    }
}
