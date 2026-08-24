<?php
// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution {
    function findSubarrays($nums) {
        $seen = [];
        $n = count($nums);
        for ($i = 0; $i + 1 < $n; $i++) {
            $s = $nums[$i] + $nums[$i + 1];
            if (isset($seen[$s])) return true;
            $seen[$s] = true;
        }
        return false;
    }
}
