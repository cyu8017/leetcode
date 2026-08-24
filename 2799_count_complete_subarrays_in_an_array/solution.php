<?php
// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution {
    function countCompleteSubarrays($nums) {
        $need = count(array_unique($nums));
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $seen = [];
            for ($j = $i; $j < $n; $j++) {
                $seen[$nums[$j]] = true;
                if (count($seen) === $need) {
                    $ans += $n - $j;
                    break;
                }
            }
        }
        return $ans;
    }
}
