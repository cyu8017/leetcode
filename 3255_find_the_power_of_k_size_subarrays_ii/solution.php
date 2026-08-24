<?php
// LeetCode 3255 - Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution {
    function resultsArray($nums, $k) {
        $n = count($nums);
        $ans = array_fill(0, $n - $k + 1, 0);
        if ($k === 1) return $nums;
        $streak = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] === $nums[$i - 1] + 1) $streak++;
            else $streak = 1;
            if ($i >= $k - 1) $ans[$i - $k + 1] = $streak >= $k ? $nums[$i] : -1;
        }
        return $ans;
    }
}
