<?php
// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

class Solution {
    function maximumValueSum($nums, $k, $edges) {
        $f0 = 0;
        $f1 = PHP_INT_MIN;
        foreach ($nums as $x) {
            $nf0 = max($f0 + $x, $f1 + ($x ^ $k));
            $nf1 = max($f1 + $x, $f0 + ($x ^ $k));
            $f0 = $nf0;
            $f1 = $nf1;
        }
        return $f0;
    }
}
