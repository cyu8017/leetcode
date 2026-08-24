<?php
// LeetCode 0976 - Largest Perimeter Triangle
// https://leetcode.com/problems/largest-perimeter-triangle/

class Solution {
    function largestPerimeter($nums) {
        sort($nums);
        for ($i = count($nums) - 1; $i >= 2; $i--) {
            if ($nums[$i] < $nums[$i - 1] + $nums[$i - 2])
                return $nums[$i] + $nums[$i - 1] + $nums[$i - 2];
        }
        return 0;
    }
}
