<?php
// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

class Solution {
    function numberOfPairs($nums) {
        $cnt = [];
        foreach ($nums as $x) $cnt[$x] = ($cnt[$x] ?? 0) + 1;
        $pairs = 0;
        $left = 0;
        foreach ($cnt as $c) {
            $pairs += intdiv($c, 2);
            $left += $c % 2;
        }
        return [$pairs, $left];
    }
}
