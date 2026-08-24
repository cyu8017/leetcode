<?php
// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution {
    function getSneakyNumbers($nums) {
        $seen = [];
        $ans = [];
        foreach ($nums as $x) {
            if (isset($seen[$x])) $ans[] = $x;
            else $seen[$x] = true;
        }
        return $ans;
    }
}
