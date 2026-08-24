<?php
// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

class Solution {
    function minOperations($nums1, $nums2) {
        $n = count($nums1);
        $ans = $this->calc($nums1, $nums2);
        $t = $nums1[$n - 1];
        $nums1[$n - 1] = $nums2[$n - 1];
        $nums2[$n - 1] = $t;
        $cand = $this->calc($nums1, $nums2) + 1;
        if ($cand < $ans) $ans = $cand;
        $nums2[$n - 1] = $nums1[$n - 1];
        $nums1[$n - 1] = $t;
        return $ans >= (1 << 30) ? -1 : $ans;
    }

    private function calc($a1, $a2) {
        $n = count($a1);
        $ops = 0;
        $last1 = $a1[$n - 1];
        $last2 = $a2[$n - 1];
        for ($i = 0; $i < $n - 1; $i++) {
            $x = $a1[$i];
            $y = $a2[$i];
            if ($x <= $last1 && $y <= $last2) continue;
            if ($y <= $last1 && $x <= $last2) { $ops++; continue; }
            return 1 << 30;
        }
        return $ops;
    }
}
