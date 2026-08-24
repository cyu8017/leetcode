<?php
// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

class Solution {
    function canTraverseAllPairs($nums) {
        $n = count($nums);
        if ($n === 1) return true;
        $mx = $nums[0];
        foreach ($nums as $x) if ($x > $mx) $mx = $x;
        $parent = range(0, $mx);
        $find = function($x) use (&$find, &$parent) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $unite = function($a, $b) use ($find, &$parent) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra !== $rb) $parent[$ra] = $rb;
        };
        $has = array_fill(0, $mx + 1, false);
        foreach ($nums as $x) {
            if ($x === 1) return false;
            $has[$x] = true;
        }
        $sieve = array_fill(0, $mx + 1, 0);
        for ($i = 2; $i <= $mx; $i++) {
            if ($sieve[$i] === 0) {
                for ($j = $i; $j <= $mx; $j += $i) {
                    if ($sieve[$j] === 0) $sieve[$j] = $i;
                    if ($has[$j]) $unite($i, $j);
                }
            }
        }
        $root = $find($nums[0]);
        foreach ($nums as $x) if ($find($x) !== $root) return false;
        return true;
    }
}
