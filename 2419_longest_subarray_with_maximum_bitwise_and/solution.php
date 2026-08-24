<?php
// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution {
    function longestSubarray($nums) {
        $mx = $nums[0];
        foreach ($nums as $x) if ($x > $mx) $mx = $x;
        $ans = 0;
        $cur = 0;
        foreach ($nums as $x) {
            if ($x === $mx) {
                $cur++;
                if ($cur > $ans) $ans = $cur;
            } else $cur = 0;
        }
        return $ans;
    }
}
