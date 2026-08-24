<?php
// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution {
    function sumCounts($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $seen = [];
            for ($j = $i; $j < $n; $j++) {
                $seen[$nums[$j]] = true;
                $d = count($seen);
                $ans += $d * $d;
            }
        }
        return $ans;
    }
}
