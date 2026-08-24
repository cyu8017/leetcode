<?php
// LeetCode 3868 - Minimum Cost to Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

class Solution {
    function minCost($nums1, $nums2) {
        $cnt2 = [];
        foreach ($nums2 as $x) $cnt2[$x] = ($cnt2[$x] ?? 0) + 1;
        $cnt1 = [];
        foreach ($nums1 as $x) {
            $c = $cnt2[$x] ?? 0;
            if ($c > 0) $cnt2[$x] = $c - 1;
            else $cnt1[$x] = ($cnt1[$x] ?? 0) + 1;
        }
        $ans = 0;
        foreach ($cnt1 as $v) {
            if ($v % 2 === 1) return -1;
            $ans += intdiv($v, 2);
        }
        foreach ($cnt2 as $v) {
            if ($v % 2 === 1) return -1;
        }
        return $ans;
    }
}
