<?php
// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

class Solution {
    function alternatingSubarray($nums) {
        $ans = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $expect = (($j - $i) % 2 === 0) ? -1 : 1;
                if ($nums[$j] - $nums[$j - 1] !== $expect) break;
                if ($nums[$i + 1] - $nums[$i] !== 1) break;
                $ans = max($ans, $j - $i + 1);
            }
        }
        return $ans;
    }
}
