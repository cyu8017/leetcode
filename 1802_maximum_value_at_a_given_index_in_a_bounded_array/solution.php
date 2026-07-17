<?php
// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $index
     * @param Integer $maxSum
     * @return Integer
     */
    function maxValue($n, $index, $maxSum) {
        $lo = 1;
        $hi = $maxSum;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            $total = $this->minSideSum($mid, $index)
                + $mid
                + $this->minSideSum($mid, $n - $index - 1);
            if ($total <= $maxSum) {
                $lo = $mid;
            } else {
                $hi = $mid - 1;
            }
        }
        return $lo;
    }

    private function minSideSum($value, $count) {
        if ($value > $count) {
            return intdiv(($value - 1 + $value - $count) * $count, 2);
        }
        return intdiv($value * ($value - 1), 2) + ($count - $value + 1);
    }
}
