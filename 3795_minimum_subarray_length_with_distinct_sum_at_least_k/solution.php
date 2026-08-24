<?php
// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

class Solution {
    function minLength($nums, $k) {
        $n = count($nums);
        $ans = $n + 1;
        $l = 0;
        $cnt = [];
        $s = 0;
        for ($r = 0; $r < $n; $r++) {
            $c = (isset($cnt[$nums[$r]]) ? $cnt[$nums[$r]] : 0) + 1;
            $cnt[$nums[$r]] = $c;
            if ($c === 1) $s += $nums[$r];
            while ($s >= $k) {
                if ($r - $l + 1 < $ans) $ans = $r - $l + 1;
                $left = $nums[$l];
                $nc = $cnt[$left] - 1;
                if ($nc === 0) {
                    unset($cnt[$left]);
                    $s -= $left;
                } else $cnt[$left] = $nc;
                $l++;
            }
        }
        return $ans > $n ? -1 : $ans;
    }
}
