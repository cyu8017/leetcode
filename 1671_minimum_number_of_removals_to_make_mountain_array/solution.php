<?php
// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution {
    function minimumMountainRemovals($nums) {
        $lis = function($a) {
            $d = [];
            $out = [];
            foreach ($a as $x) {
                $lo = 0;
                $hi = count($d);
                while ($lo < $hi) {
                    $mid = intdiv($lo + $hi, 2);
                    if ($d[$mid] < $x) $lo = $mid + 1;
                    else $hi = $mid;
                }
                if ($lo === count($d)) $d[] = $x;
                else $d[$lo] = $x;
                $out[] = $lo + 1;
            }
            return $out;
        };
        $l = $lis($nums);
        $r = array_reverse($lis(array_reverse($nums)));
        $n = count($nums);
        $best = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($l[$i] > 1 && $r[$i] > 1) {
                $best = max($best, $l[$i] + $r[$i] - 1);
            }
        }
        return $n - $best;
    }
}
