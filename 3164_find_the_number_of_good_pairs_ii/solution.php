<?php
// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

class Solution {
    function numberOfPairs($nums1, $nums2, $k) {
        $cnt1 = [];
        foreach ($nums1 as $x) {
            if ($x % $k === 0) {
                $v = intdiv($x, $k);
                $cnt1[$v] = ($cnt1[$v] ?? 0) + 1;
            }
        }
        if (!$cnt1) return 0;
        $cnt2 = [];
        foreach ($nums2 as $x) $cnt2[$x] = ($cnt2[$x] ?? 0) + 1;
        $mx = 0;
        foreach ($cnt1 as $x => $_) $mx = max($mx, $x);
        $ans = 0;
        foreach ($cnt2 as $x => $v) {
            $s = 0;
            for ($y = $x; $y <= $mx; $y += $x) {
                if (isset($cnt1[$y])) $s += $cnt1[$y];
            }
            $ans += $s * $v;
        }
        return $ans;
    }
}
