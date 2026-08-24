<?php
// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

class Solution {
    function subarraySum($nums) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $start = $i - $nums[$i];
            if ($start < 0) $start = 0;
            $ans += $pref[$i + 1] - $pref[$start];
        }
        return $ans;
    }
}
