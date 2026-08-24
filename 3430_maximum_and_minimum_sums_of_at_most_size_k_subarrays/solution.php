<?php
// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

class Solution {
    function minMaxSubarraySum($nums, $k) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $mn = $nums[$i];
            $mx = $nums[$i];
            for ($j = $i; $j < $n && $j - $i + 1 <= $k; $j++) {
                if ($nums[$j] < $mn) $mn = $nums[$j];
                if ($nums[$j] > $mx) $mx = $nums[$j];
                $ans += $mn + $mx;
            }
        }
        return $ans;
    }
}
