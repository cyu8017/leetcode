<?php
// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

class Solution {
    function minOperations($nums) {
        $g = [];
        foreach ($nums as $x) {
            $l = 0;
            $r = count($g);
            while ($l < $r) {
                $mid = ($l + $r) >> 1;
                if ($g[$mid] < $x) $r = $mid;
                else $l = $mid + 1;
            }
            if ($l === count($g)) $g[] = $x;
            else $g[$l] = $x;
        }
        return count($g);
    }
}
