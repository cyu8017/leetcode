<?php
// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

class Solution {
    function maximumSubarraySum($nums, $k) {
        $p = [];
        $p[$nums[0]] = 0;
        $s = 0;
        $n = count($nums);
        $ans = null;
        for ($i = 0; $i < $n; $i++) {
            $s += $nums[$i];
            if (isset($p[$nums[$i] - $k])) {
                $cand = $s - $p[$nums[$i] - $k];
                if ($ans === null || $cand > $ans) $ans = $cand;
            }
            if (isset($p[$nums[$i] + $k])) {
                $cand = $s - $p[$nums[$i] + $k];
                if ($ans === null || $cand > $ans) $ans = $cand;
            }
            if ($i + 1 === $n) break;
            if (!isset($p[$nums[$i + 1]]) || $s < $p[$nums[$i + 1]]) $p[$nums[$i + 1]] = $s;
        }
        return $ans === null ? 0 : $ans;
    }
}
