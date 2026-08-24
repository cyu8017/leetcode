<?php
// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

class Solution {
    function minOperations($nums1, $nums2) {
        $ans = 1;
        $n = count($nums1);
        $ok = false;
        $d = 1 << 30;
        for ($i = 0; $i < $n; $i++) {
            $x = max($nums1[$i], $nums2[$i]);
            $y = min($nums1[$i], $nums2[$i]);
            $ans += $x - $y;
            $d = min($d, min(abs($x - $nums2[$n]), abs($y - $nums2[$n])));
            if ($nums2[$n] >= $y && $nums2[$n] <= $x) $ok = true;
        }
        if (!$ok) $ans += $d;
        return $ans;
    }
}
