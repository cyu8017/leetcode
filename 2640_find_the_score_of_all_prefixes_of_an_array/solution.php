<?php
// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution {
    function findPrefixScore($nums) {
        $ans = [];
        $mx = 0;
        $sum = 0;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] > $mx) $mx = $nums[$i];
            $sum += $nums[$i] + $mx;
            $ans[$i] = $sum;
        }
        return $ans;
    }
}
