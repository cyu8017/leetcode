<?php
// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

class Solution {
    private $parent;
    private $sum;

    function maximumSegmentSum($nums, $removeQueries) {
        $n = count($nums);
        $this->parent = range(0, $n - 1);
        $this->sum = array_fill(0, $n, 0);
        $active = array_fill(0, $n, false);
        $ans = array_fill(0, $n, 0);
        $best = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $ans[$i] = $best;
            $idx = $removeQueries[$i];
            $active[$idx] = true;
            $this->sum[$idx] = $nums[$idx];
            if ($idx > 0 && $active[$idx - 1]) $this->unite($idx, $idx - 1);
            if ($idx + 1 < $n && $active[$idx + 1]) $this->unite($idx, $idx + 1);
            $best = max($best, $this->sum[$this->find($idx)]);
        }
        return $ans;
    }

    private function find($x) {
        if ($this->parent[$x] !== $x) $this->parent[$x] = $this->find($this->parent[$x]);
        return $this->parent[$x];
    }

    private function unite($a, $b) {
        $ra = $this->find($a);
        $rb = $this->find($b);
        if ($ra === $rb) return;
        $this->parent[$rb] = $ra;
        $this->sum[$ra] += $this->sum[$rb];
    }
}
