<?php
// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

class Solution {
    function largestPerimeter($nums) {
        sort($nums);
        $sum = 0;
        foreach ($nums as $v) $sum += $v;
        for ($i = count($nums) - 1; $i >= 2; $i--) {
            $sum -= $nums[$i];
            if ($sum > $nums[$i]) return $sum + $nums[$i];
        }
        return -1;
    }
}
