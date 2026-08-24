<?php
// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

class Solution {
    function maximumMatchingIndices($nums1, $nums2) {
        $n = count($nums1);
        $ans = 0;
        for ($shift = 0; $shift < $n; $shift++) {
            $cnt = 0;
            for ($i = 0; $i < $n; $i++) {
                if ($nums1[($i - $shift + $n) % $n] === $nums2[$i]) $cnt++;
            }
            if ($cnt > $ans) $ans = $cnt;
        }
        return $ans;
    }
}
