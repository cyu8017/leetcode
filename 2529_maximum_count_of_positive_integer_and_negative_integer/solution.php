<?php
// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution {
    function maximumCount($nums) {
        $pos = 0;
        $neg = 0;
        foreach ($nums as $x) {
            if ($x > 0) $pos++;
            else if ($x < 0) $neg++;
        }
        return max($pos, $neg);
    }
}
