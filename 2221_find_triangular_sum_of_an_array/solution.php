<?php
// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution {
    function triangularSum($nums) {
        while (count($nums) > 1) {
            $next = [];
            $n = count($nums);
            for ($i = 0; $i < $n - 1; $i++)
                $next[] = ($nums[$i] + $nums[$i + 1]) % 10;
            $nums = $next;
        }
        return $nums[0];
    }
}
