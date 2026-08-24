<?php
// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

class Solution {
    function countAlternatingSubarrays($nums) {
        $ans = 1;
        $s = 1;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] !== $nums[$i - 1]) $s++;
            else $s = 1;
            $ans += $s;
        }
        return $ans;
    }
}
