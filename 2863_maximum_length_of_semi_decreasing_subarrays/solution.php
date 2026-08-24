<?php
// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

class Solution {
    function maxSubarrayLength($nums) {
        $n = count($nums);
        $ans = 0;
        $st = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            if (!count($st) || $nums[$i] > $nums[$st[count($st) - 1]]) $st[] = $i;
        }
        for ($i = 0; $i < $n; $i++) {
            while (count($st) && $nums[$i] > $nums[$st[count($st) - 1]]) {
                $j = array_pop($st);
                if ($j - $i + 1 > $ans) $ans = $j - $i + 1;
            }
        }
        return $ans;
    }
}
