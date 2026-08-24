<?php
// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

class Solution {
    public $previous;
    public $current;
    public $prefix;
    public $INF;
    function value($left, $right) {
        $sum = $this->prefix[$right] - $this->prefix[$left];
        return $sum * ($sum + 1) / 2;
    }
    function compute($lo, $hi, $optLo, $optHi) {
        if ($lo > $hi) return;
        $mid = ($lo + $hi) >> 1;
        $bestIndex = -1;
        $end = min($optHi, $mid - 1);
        for ($split = $optLo; $split <= $end; $split++) {
            if ($this->previous[$split] === $this->INF) continue;
            $candidate = $this->previous[$split] + $this->value($split, $mid);
            if ($candidate < $this->current[$mid]) {
                $this->current[$mid] = $candidate;
                $bestIndex = $split;
            }
        }
        if ($bestIndex === -1) $bestIndex = $optLo;
        $this->compute($lo, $mid - 1, $optLo, $bestIndex);
        $this->compute($mid + 1, $hi, $bestIndex, $optHi);
    }
    function minPartitionScore($nums, $k) {
        $n = count($nums);
        $this->INF = PHP_INT_MAX / 4;
        $this->prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $this->prefix[$i + 1] = $this->prefix[$i] + $nums[$i];
        $this->previous = array_fill(0, $n + 1, $this->INF);
        $this->previous[0] = 0;
        for ($parts = 1; $parts <= $k; $parts++) {
            $this->current = array_fill(0, $n + 1, $this->INF);
            $this->compute($parts, $n, $parts - 1, $n - 1);
            $this->previous = $this->current;
        }
        return $this->previous[$n];
    }
}
