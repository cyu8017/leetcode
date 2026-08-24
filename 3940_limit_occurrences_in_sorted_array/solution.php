<?php
// LeetCode 3940 - Limit Occurrences In Sorted Array
// https://leetcode.com/problems/limit-occurrences-in-sorted-array/

class Solution {
    function limitOccurrences($nums, $k) {
        $n = count($nums);
        $cnt = 1;
        $l = 1;
        for ($r = 1; $r < $n; $r++) {
            if ($nums[$r] !== $nums[$r - 1]) $cnt = 1;
            else $cnt++;
            if ($cnt <= $k) {
                $nums[$l] = $nums[$r];
                $l++;
            }
        }
        return array_slice($nums, 0, $l);
    }
}
