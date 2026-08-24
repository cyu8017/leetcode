<?php
// LeetCode 3985 - Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/

class Solution {
    function maxPalindromicSubarraySum($nums) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        $odd = array_fill(0, $n, 0);
        $left = 0;
        $right = -1;
        for ($i = 0; $i < $n; $i++) {
            $radius = 1;
            if ($i <= $right) {
                $mirror = $left + $right - $i;
                $radius = $odd[$mirror];
                if ($right - $i + 1 < $radius) $radius = $right - $i + 1;
            }
            while ($i - $radius >= 0 && $i + $radius < $n && $nums[$i - $radius] == $nums[$i + $radius]) $radius++;
            $odd[$i] = $radius;
            if ($i + $radius - 1 > $right) {
                $left = $i - $radius + 1;
                $right = $i + $radius - 1;
            }
        }
        $even = array_fill(0, $n, 0);
        $left = 0;
        $right = -1;
        for ($i = 0; $i < $n; $i++) {
            $radius = 0;
            if ($i <= $right) {
                $mirror = $left + $right - $i + 1;
                $radius = $even[$mirror];
                if ($right - $i + 1 < $radius) $radius = $right - $i + 1;
            }
            while ($i - $radius - 1 >= 0 && $i + $radius < $n && $nums[$i - $radius - 1] == $nums[$i + $radius]) $radius++;
            $even[$i] = $radius;
            if ($i + $radius - 1 > $right) {
                $left = $i - $radius;
                $right = $i + $radius - 1;
            }
        }
        $answer = 0;
        for ($i = 0; $i < $n; $i++) {
            $sum = $prefix[$i + $odd[$i]] - $prefix[$i - $odd[$i] + 1];
            if ($sum > $answer) $answer = $sum;
            if ($even[$i] > 0) {
                $sum = $prefix[$i + $even[$i]] - $prefix[$i - $even[$i]];
                if ($sum > $answer) $answer = $sum;
            }
        }
        return $answer;
    }
}
