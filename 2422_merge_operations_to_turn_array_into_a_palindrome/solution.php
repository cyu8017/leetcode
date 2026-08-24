<?php
// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

class Solution {
    function minimumOperations($nums) {
        $l = 0;
        $r = count($nums) - 1;
        $left = $nums[$l];
        $right = $nums[$r];
        $ans = 0;
        while ($l < $r) {
            if ($left === $right) {
                $l++;
                $r--;
                if ($l < $r) {
                    $left = $nums[$l];
                    $right = $nums[$r];
                }
            } elseif ($left < $right) {
                $l++;
                $left += $nums[$l];
                $ans++;
            } else {
                $r--;
                $right += $nums[$r];
                $ans++;
            }
        }
        return $ans;
    }
}
