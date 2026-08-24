<?php
// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

class Solution {
    function longestSubarray($nums, $k) {
        $cnt = [];
        $ans = 0;
        $cur = 0;
        $l = 0;
        $n = count($nums);
        for ($r = 0; $r < $n; $r++) {
            $c = (isset($cnt[$nums[$r]]) ? $cnt[$nums[$r]] : 0) + 1;
            $cnt[$nums[$r]] = $c;
            if ($c === 2) $cur++;
            while ($cur > $k) {
                $c2 = (isset($cnt[$nums[$l]]) ? $cnt[$nums[$l]] : 0) - 1;
                $cnt[$nums[$l]] = $c2;
                if ($c2 === 1) $cur--;
                $l++;
            }
            $ans = max($ans, $r - $l + 1);
        }
        return $ans;
    }
}
