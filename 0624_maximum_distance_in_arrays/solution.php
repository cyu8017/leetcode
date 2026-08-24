<?php
// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution {
    function maxDistance($arrays) {
        $minVal = $arrays[0][0];
        $maxVal = $arrays[0][count($arrays[0]) - 1];
        $best = 0;
        for ($i = 1; $i < count($arrays); ++$i) {
            $arr = $arrays[$i];
            $first = $arr[0];
            $last = $arr[count($arr) - 1];
            $best = max($best, abs($last - $minVal), abs($maxVal - $first));
            $minVal = min($minVal, $first);
            $maxVal = max($maxVal, $last);
        }
        return $best;
    }
}
