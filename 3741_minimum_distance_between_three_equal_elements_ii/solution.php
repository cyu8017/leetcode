<?php
// LeetCode 3741 - Minimum Distance Between Three Equal Elements II
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

class Solution {
    function minimumDistance($nums) {
        $g = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (!isset($g[$nums[$i]])) $g[$nums[$i]] = [];
            $g[$nums[$i]][] = $i;
        }
        $inf = 1 << 30;
        $ans = $inf;
        foreach ($g as $ls) {
            $m = count($ls);
            for ($h = 0; $h < $m - 2; $h++) {
                $ans = min($ans, ($ls[$h + 2] - $ls[$h]) * 2);
            }
        }
        return $ans === $inf ? -1 : $ans;
    }
}
