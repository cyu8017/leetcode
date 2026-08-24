<?php
// LeetCode 3862 - Find the Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

class Solution {
    function smallestBalancedIndex($nums) {
        $s = 0;
        $p = 1;
        foreach ($nums as $x) $s += $x;
        for ($i = count($nums) - 1; $i >= 0; $i--) {
            $s -= $nums[$i];
            if ($s === $p) return $i;
            $p *= $nums[$i];
            if ($p >= $s) break;
        }
        return -1;
    }
}
