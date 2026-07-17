<?php
// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumMinProduct($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);

        foreach ($nums as $index => $value) {
            $prefix[$index + 1] = $prefix[$index] + $value;
        }

        $leftBound = array_fill(0, $n, -1);
        $stack = [];
        foreach ($nums as $index => $value) {
            while (!empty($stack) && $nums[$stack[count($stack) - 1]] >= $value) {
                array_pop($stack);
            }
            $leftBound[$index] = empty($stack) ? -1 : $stack[count($stack) - 1];
            $stack[] = $index;
        }

        $rightBound = array_fill(0, $n, $n);
        $stack = [];
        for ($index = $n - 1; $index >= 0; $index--) {
            $value = $nums[$index];
            while (!empty($stack) && $nums[$stack[count($stack) - 1]] >= $value) {
                array_pop($stack);
            }
            $rightBound[$index] = empty($stack) ? $n : $stack[count($stack) - 1];
            $stack[] = $index;
        }

        $best = 0;
        foreach ($nums as $index => $value) {
            $total = $prefix[$rightBound[$index]] - $prefix[$leftBound[$index] + 1];
            $best = max($best, $total * $value);
        }

        return $best % $mod;
    }
}
