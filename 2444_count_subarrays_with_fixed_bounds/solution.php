<?php
// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution {
    function countSubarrays($nums, $minK, $maxK) {
        $ans = 0;
        $imin = -1;
        $imax = -1;
        $ibad = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($x < $minK || $x > $maxK) $ibad = $i;
            if ($x === $minK) $imin = $i;
            if ($x === $maxK) $imax = $i;
            $bound = $imin < $imax ? $imin : $imax;
            if ($bound > $ibad) $ans += $bound - $ibad;
        }
        return $ans;
    }
}
