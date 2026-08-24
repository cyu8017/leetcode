<?php
// LeetCode 3804 - Number of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

class Solution {
    function centeredSubarrays($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $st = [];
            $s = 0;
            for ($j = $i; $j < $n; $j++) {
                $s += $nums[$j];
                $st[$nums[$j]] = true;
                if (isset($st[$s])) $ans++;
            }
        }
        return $ans;
    }
}
