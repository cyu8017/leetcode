<?php
// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution {
    function countFairPairs($nums, $lower, $upper) {
        sort($nums);
        $count = function($x) use ($nums) {
            $ans = 0;
            $l = 0;
            $r = count($nums) - 1;
            while ($l < $r) {
                if ($nums[$l] + $nums[$r] <= $x) {
                    $ans += $r - $l;
                    $l++;
                } else $r--;
            }
            return $ans;
        };
        return $count($upper) - $count($lower - 1);
    }
}
