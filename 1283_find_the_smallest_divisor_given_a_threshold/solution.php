<?php
// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $threshold
     * @return Integer
     */
    function smallestDivisor($nums, $threshold) {
        $lo = 1;
        $hi = max($nums);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $sum = 0;
            foreach ($nums as $x) $sum += intdiv($x + $mid - 1, $mid);
            if ($sum <= $threshold) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
