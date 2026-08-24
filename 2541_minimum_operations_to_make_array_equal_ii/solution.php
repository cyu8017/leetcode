<?php
// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

class Solution {
    function minOperations($nums1, $nums2, $k) {
        $n = count($nums1);
        if ($k === 0) {
            for ($i = 0; $i < $n; $i++) {
                if ($nums1[$i] !== $nums2[$i]) return -1;
            }
            return 0;
        }
        $pos = 0;
        $neg = 0;
        for ($i = 0; $i < $n; $i++) {
            $d = $nums1[$i] - $nums2[$i];
            if ($d % $k !== 0) return -1;
            if ($d > 0) $pos += intdiv($d, $k);
            else $neg += intdiv(-$d, $k);
        }
        return $pos !== $neg ? -1 : $pos;
    }
}
