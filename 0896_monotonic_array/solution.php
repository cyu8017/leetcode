<?php
// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

class Solution {
    function isMonotonic($nums) {
        $inc = true;
        $dec = true;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] < $nums[$i - 1]) $inc = false;
            if ($nums[$i] > $nums[$i - 1]) $dec = false;
        }
        return $inc || $dec;
    }
}
