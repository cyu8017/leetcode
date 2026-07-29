<?php
// LeetCode 1052 - Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution {
    /**
     * @param Integer[] $customers
     * @param Integer[] $grumpy
     * @param Integer $minutes
     * @return Integer
     */
    function maxSatisfied($customers, $grumpy, $minutes) {
        $base = 0;
        $n = count($customers);
        for ($i = 0; $i < $n; $i++) {
            if ($grumpy[$i] === 0) {
                $base += $customers[$i];
            }
        }
        $gain = 0;
        $best = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($grumpy[$i]) {
                $gain += $customers[$i];
            }
            if ($i >= $minutes && $grumpy[$i - $minutes]) {
                $gain -= $customers[$i - $minutes];
            }
            $best = max($best, $gain);
        }
        return $base + $best;
    }
}
