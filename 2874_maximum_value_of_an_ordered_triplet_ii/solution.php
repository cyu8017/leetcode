<?php
// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

class Solution {
    function maximumTripletValue($nums) {
        $ans = 0;
        $maxI = 0;
        $maxDiff = 0;
        foreach ($nums as $v) {
            if ($maxDiff * $v > $ans) $ans = $maxDiff * $v;
            if ($maxI - $v > $maxDiff) $maxDiff = $maxI - $v;
            if ($v > $maxI) $maxI = $v;
        }
        return $ans;
    }
}
