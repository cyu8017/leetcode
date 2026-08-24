<?php
// LeetCode 3392 - Count Subarrays of Length Three With a Condition
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

class Solution {
    function countSubarrays($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i + 2 < $n; $i++) {
            if ($nums[$i] * 2 + $nums[$i + 2] * 2 === $nums[$i + 1]) $ans++;
        }
        return $ans;
    }
}
