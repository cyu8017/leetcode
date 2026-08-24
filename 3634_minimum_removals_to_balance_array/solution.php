<?php
// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution {
    function minRemoval($nums, $k) {
        sort($nums);
        $n = count($nums);
        $lowerBound = function($a, $target) {
            $lo = 0;
            $hi = count($a);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($a[$mid] < $target) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $cnt = 0;
        for ($i = 0; $i < $n; $i++) {
            $j = $n;
            if ($nums[$i] * $k <= $nums[$n - 1]) {
                $target = $nums[$i] * $k + 1;
                $j = $lowerBound($nums, $target);
            }
            $cnt = max($cnt, $j - $i);
        }
        return $n - $cnt;
    }
}
