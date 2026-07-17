<?php
// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

class Solution {
    /**
     * @param Integer[] $flowers
     * @return Integer
     */
    function maximumBeauty($flowers) {
        $first = [];
        $prefix = [0];
        foreach ($flowers as $value) {
            $prefix[] = $prefix[count($prefix) - 1] + max($value, 0);
        }
        $best = PHP_INT_MIN;
        foreach ($flowers as $i => $value) {
            if (array_key_exists($value, $first)) {
                $left = $first[$value];
                $between = $prefix[$i] - $prefix[$left + 1];
                $candidate = $flowers[$left] + $flowers[$i] + $between;
                if ($candidate > $best) {
                    $best = $candidate;
                }
            } else {
                $first[$value] = $i;
            }
        }
        return $best;
    }
}
