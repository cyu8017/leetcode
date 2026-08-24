<?php
// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution {
    function maximumSubarraySum($nums, $k) {
        $cnt = [];
        $sum = 0;
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $sum += $nums[$i];
            if (!isset($cnt[$nums[$i]])) $cnt[$nums[$i]] = 0;
            $cnt[$nums[$i]]++;
            if ($i >= $k) {
                $y = $nums[$i - $k];
                $sum -= $y;
                $c = $cnt[$y] - 1;
                if ($c === 0) unset($cnt[$y]);
                else $cnt[$y] = $c;
            }
            if ($i >= $k - 1 && count($cnt) === $k && $sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
