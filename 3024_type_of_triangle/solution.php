<?php
// LeetCode 3024 - Type of Triangle
// https://leetcode.com/problems/type-of-triangle/

class Solution {
    function triangleType($nums) {
        sort($nums);
        if ($nums[0] + $nums[1] <= $nums[2]) return "none";
        if ($nums[0] === $nums[2]) return "equilateral";
        if ($nums[0] === $nums[1] || $nums[1] === $nums[2]) return "isosceles";
        return "scalene";
    }
}
