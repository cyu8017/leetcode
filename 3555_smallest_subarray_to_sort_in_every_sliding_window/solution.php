<?php
// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

class Solution {
    private function f($nums, $i, $j, $inf) {
        $mi = $inf;
        $mx = -$inf;
        $l = -1;
        $r = -1;
        for ($p = $i; $p <= $j; $p++) {
            if ($nums[$p] < $mx) $r = $p;
            else $mx = $nums[$p];
            $q = $j - $p + $i;
            if ($nums[$q] > $mi) $l = $q;
            else $mi = $nums[$q];
        }
        if ($r === -1) return 0;
        return $r - $l + 1;
    }

    function minSubarraySort($nums, $k) {
        $inf = 1 << 30;
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i <= $n - $k; $i++) $ans[] = $this->f($nums, $i, $i + $k - 1, $inf);
        return $ans;
    }
}
