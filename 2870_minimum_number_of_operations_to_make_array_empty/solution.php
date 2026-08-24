<?php
// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

class Solution {
    function minOperations($nums) {
        $freq = [];
        foreach ($nums as $v) {
            if (!isset($freq[$v])) $freq[$v] = 0;
            $freq[$v]++;
        }
        $ans = 0;
        foreach ($freq as $c) {
            if ($c === 1) return -1;
            $ans += intdiv($c + 2, 3);
        }
        return $ans;
    }
}
