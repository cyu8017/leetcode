<?php
// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

class Solution {
    private function upperBound($a, $target) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($a[$mid] <= $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function countInv($nums, $k, $threshold) {
        $sorted = [];
        $inv = 0;
        foreach ($nums as $num) {
            $left = $this->upperBound($sorted, $num);
            $right = $this->upperBound($sorted, $num + $threshold);
            $inv += $right - $left;
            array_splice($sorted, $this->upperBound($sorted, $num), 0, [$num]);
        }
        return $inv >= $k;
    }

    function minThreshold($nums, $k) {
        $mx = 0;
        foreach ($nums as $v) if ($v > $mx) $mx = $v;
        $l = 0;
        $r = $mx + 1;
        while ($l < $r) {
            $m = ($l + $r) >> 1;
            if ($this->countInv($nums, $k, $m)) $r = $m;
            else $l = $m + 1;
        }
        return $l > $mx ? -1 : $l;
    }
}
