<?php
// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

class Solution {
    function minDistinctFreqPair($nums) {
        $cnt = [];
        foreach ($nums as $v) $cnt[$v] = ($cnt[$v] ?? 0) + 1;
        $x = $nums[0];
        foreach ($nums as $v) $x = min($x, $v);
        $minY = PHP_INT_MAX;
        foreach ($cnt as $y => $_) {
            if ($y < $minY && $cnt[$x] !== $cnt[$y]) $minY = $y;
        }
        if ($minY === PHP_INT_MAX) return [-1, -1];
        return [$x, $minY];
    }
}
