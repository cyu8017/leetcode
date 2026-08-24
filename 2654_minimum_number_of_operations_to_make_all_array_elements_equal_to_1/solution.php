<?php
// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

class Solution {
    function minOperations($nums) {
        $gcd = function($a, $b) {
            while ($b) { $t = $a % $b; $a = $b; $b = $t; }
            return $a;
        };
        $n = count($nums);
        $ones = 0;
        foreach ($nums as $x) if ($x === 1) $ones++;
        if ($ones > 0) return $n - $ones;
        $best = $n + 1;
        for ($i = 0; $i < $n; $i++) {
            $g = 0;
            for ($j = $i; $j < $n; $j++) {
                $g = $gcd($g, $nums[$j]);
                if ($g === 1) { $best = min($best, $j - $i); break; }
            }
        }
        if ($best === $n + 1) return -1;
        return $best + $n - 1;
    }
}
