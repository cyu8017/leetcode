<?php
// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

class CountIntervals {
    private $ivs = [];
    private $cnt = 0;

    function __construct() {
        $this->ivs = [];
        $this->cnt = 0;
    }

    function add($left, $right) {
        $merged = [];
        foreach ($this->ivs as $iv) {
            if ($iv[1] + 1 < $left || $iv[0] - 1 > $right) {
                $merged[] = $iv;
            } else {
                $left = min($left, $iv[0]);
                $right = max($right, $iv[1]);
                $this->cnt -= $iv[1] - $iv[0] + 1;
            }
        }
        $merged[] = [$left, $right];
        usort($merged, function ($a, $b) { return $a[0] <=> $b[0]; });
        $this->ivs = $merged;
        $this->cnt += $right - $left + 1;
    }

    function count() {
        return $this->cnt;
    }
}
