<?php
// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

class Solution {
    function findPeaks($mountain) {
        $ans = [];
        for ($i = 1; $i + 1 < count($mountain); $i++) {
            if ($mountain[$i] > $mountain[$i - 1] && $mountain[$i] > $mountain[$i + 1]) {
                $ans[] = $i;
            }
        }
        return $ans;
    }
}
