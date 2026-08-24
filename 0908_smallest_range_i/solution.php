<?php
// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

class Solution {
    function smallestRangeI($nums, $k) {
        return max(0, max($nums) - min($nums) - 2 * $k);
    }
}
