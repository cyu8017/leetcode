<?php
// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

class Solution {
    function numberOfPoints($nums) {
        $cov = array_fill(0, 102, 0);
        foreach ($nums as $ab) {
            for ($x = $ab[0]; $x <= $ab[1]; $x++) $cov[$x] = 1;
        }
        $s = 0;
        foreach ($cov as $v) $s += $v;
        return $s;
    }
}
