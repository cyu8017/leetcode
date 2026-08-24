<?php
// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

class Solution {
    function maxSumDistinctTriplet($x, $y) {
        $n = count($x);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$x[$i], $y[$i]];
        usort($arr, function($a, $b) { return $b[1] <=> $a[1]; });
        $ans = 0;
        $vis = [];
        for ($i = 0; $i < $n; $i++) {
            $a = $arr[$i][0];
            $b = $arr[$i][1];
            if (!isset($vis[$a])) {
                $vis[$a] = true;
                $ans += $b;
                if (count($vis) === 3) return $ans;
            }
        }
        return -1;
    }
}
