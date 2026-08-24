<?php
// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

class Solution {
    public $ts = [];
    function maximumTripletValue($nums) {
        $n = count($nums);
        $right = array_fill(0, $n, 0);
        $right[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $right[$i] = max($nums[$i], $right[$i + 1]);
        $this->ts = [];
        $this->add($nums[0]);
        $ans = 0;
        for ($j = 1; $j < $n - 1; $j++) {
            if ($right[$j + 1] > $nums[$j]) {
                $it = $this->lower($nums[$j]);
                if ($it !== null) $ans = max($ans, $it - $nums[$j] + $right[$j + 1]);
            }
            $this->add($nums[$j]);
        }
        return $ans;
    }
    function add($x) {
        $ts = &$this->ts;
        $lo = 0;
        $hi = count($ts);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($ts[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        if ($lo === count($ts) || $ts[$lo] !== $x) array_splice($ts, $lo, 0, [$x]);
    }
    function lower($x) {
        $ts = $this->ts;
        $lo = 0;
        $hi = count($ts);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($ts[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo > 0 ? $ts[$lo - 1] : null;
    }
}
