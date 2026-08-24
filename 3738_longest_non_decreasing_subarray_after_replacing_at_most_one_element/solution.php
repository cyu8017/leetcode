<?php
// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

class Solution {
    function longestSubarray($nums) {
        $n = count($nums);
        $left = array_fill(0, $n, 1);
        $right = array_fill(0, $n, 1);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] >= $nums[$i - 1]) $left[$i] = $left[$i - 1] + 1;
        }
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nums[$i] <= $nums[$i + 1]) $right[$i] = $right[$i + 1] + 1;
        }
        $ans = 0;
        foreach ($left as $v) $ans = max($ans, $v);
        for ($i = 0; $i < $n; $i++) {
            $a = $i > 0 ? $left[$i - 1] : 0;
            $b = $i + 1 < $n ? $right[$i + 1] : 0;
            if ($i > 0 && $i + 1 < $n && $nums[$i - 1] > $nums[$i + 1]) {
                $ans = max($ans, max($a + 1, $b + 1));
            } else {
                $ans = max($ans, $a + $b + 1);
            }
        }
        return $ans;
    }
}
