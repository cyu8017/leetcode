<?php
// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

class Solution {
    function minimumAverage($nums) {
        sort($nums);
        $n = count($nums);
        $ans = 1 << 30;
        for ($i = 0; $i * 2 < $n; $i++) $ans = min($ans, $nums[$i] + $nums[$n - $i - 1]);
        return $ans / 2.0;
    }
}
