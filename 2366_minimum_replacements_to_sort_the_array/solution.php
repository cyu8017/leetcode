<?php
// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution {
    function minimumReplacement($nums) {
        $ans = 0;
        $n = count($nums);
        $prev = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nums[$i] <= $prev) { $prev = $nums[$i]; continue; }
            $parts = intdiv($nums[$i] + $prev - 1, $prev);
            $ans += $parts - 1;
            $prev = intdiv($nums[$i], $parts);
        }
        return $ans;
    }
}
