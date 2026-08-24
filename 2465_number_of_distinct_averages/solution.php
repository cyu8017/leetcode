<?php
// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

class Solution {
    function distinctAverages($nums) {
        sort($nums);
        $seen = [];
        $l = 0;
        $r = count($nums) - 1;
        while ($l < $r) {
            $seen[$nums[$l] + $nums[$r]] = true;
            $l++;
            $r--;
        }
        return count($seen);
    }
}
