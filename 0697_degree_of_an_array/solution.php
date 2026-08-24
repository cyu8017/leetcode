<?php
// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

class Solution {
    function findShortestSubArray($nums) {
        $first = [];
        $last = [];
        $count = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (!array_key_exists($nums[$i], $first)) $first[$nums[$i]] = $i;
            $last[$nums[$i]] = $i;
            $count[$nums[$i]] = ($count[$nums[$i]] ?? 0) + 1;
        }
        $degree = 0;
        foreach ($count as $freq) $degree = max($degree, $freq);
        $best = PHP_INT_MAX;
        foreach ($count as $key => $value) {
            if ($value === $degree) $best = min($best, $last[$key] - $first[$key] + 1);
        }
        return $best;
    }
}
