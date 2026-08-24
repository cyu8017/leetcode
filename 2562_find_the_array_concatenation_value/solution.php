<?php
// LeetCode 2562 - Find the Array Concatenation Value
// https://leetcode.com/problems/find-the-array-concatenation-value/

class Solution {
    function findTheArrayConcVal($nums) {
        $ans = 0;
        $l = 0;
        $r = count($nums) - 1;
        while ($l <= $r) {
            if ($l === $r) {
                $ans += $nums[$l];
                break;
            }
            $left = $nums[$l];
            $right = $nums[$r];
            $pow = 1;
            for ($t = $right; $t > 0; $t = intdiv($t, 10)) $pow *= 10;
            $ans += $left * $pow + $right;
            $l++;
            $r--;
        }
        return $ans;
    }
}
