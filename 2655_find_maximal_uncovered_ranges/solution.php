<?php
// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

class Solution {
    function findMaximalUncoveredRanges($n, $ranges) {
        usort($ranges, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = [];
        $cur = 0;
        foreach ($ranges as $r) {
            if ($r[0] > $cur) $ans[] = [$cur, $r[0] - 1];
            if ($r[1] + 1 > $cur) $cur = $r[1] + 1;
        }
        if ($cur < $n) $ans[] = [$cur, $n - 1];
        return $ans;
    }
}
