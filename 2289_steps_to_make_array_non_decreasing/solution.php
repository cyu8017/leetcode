<?php
// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

class Solution {
    function totalSteps($nums) {
        $stack = [];
        $ans = 0;
        for ($i = count($nums) - 1; $i >= 0; $i--) {
            $steps = 0;
            while (count($stack) && $nums[$i] > $stack[count($stack) - 1][0]) {
                $steps = max($steps, $stack[count($stack) - 1][1]);
                array_pop($stack);
                $steps++;
            }
            $ans = max($ans, $steps);
            $stack[] = [$nums[$i], $steps];
        }
        return $ans;
    }
}
