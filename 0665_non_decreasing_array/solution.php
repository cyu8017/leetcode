<?php
// LeetCode 0665 - Non-decreasing Array
// https://leetcode.com/problems/non-decreasing-array/

class Solution {
    function checkPossibility($nums) {
        $changed = false;
        for ($i = 1; $i < count($nums); ++$i) {
            if ($nums[$i] >= $nums[$i - 1]) continue;
            if ($changed) return false;
            $changed = true;
            if ($i >= 2 && $nums[$i] < $nums[$i - 2]) $nums[$i] = $nums[$i - 1];
            else $nums[$i - 1] = $nums[$i];
        }
        return true;
    }
}
