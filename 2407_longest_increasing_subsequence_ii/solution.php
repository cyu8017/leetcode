<?php
// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

class Solution {
    private $tree;

    function lengthOfLIS($nums, $k) {
        $maxV = 0;
        foreach ($nums as $x) $maxV = max($maxV, $x);
        $this->tree = array_fill(0, 4 * ($maxV + 1), 0);
        $ans = 0;
        foreach ($nums as $x) {
            $lo = max(1, $x - $k);
            $best = 1;
            if ($lo <= $x - 1) $best = $this->query(1, 1, $maxV, $lo, $x - 1) + 1;
            $this->update(1, 1, $maxV, $x, $best);
            $ans = max($ans, $best);
        }
        return $ans;
    }

    private function update($idx, $l, $r, $pos, $val) {
        if ($l === $r) {
            $this->tree[$idx] = max($this->tree[$idx], $val);
            return;
        }
        $mid = ($l + $r) >> 1;
        if ($pos <= $mid) $this->update($idx * 2, $l, $mid, $pos, $val);
        else $this->update($idx * 2 + 1, $mid + 1, $r, $pos, $val);
        $this->tree[$idx] = max($this->tree[$idx * 2], $this->tree[$idx * 2 + 1]);
    }

    private function query($idx, $l, $r, $ql, $qr) {
        if ($qr < $l || $r < $ql) return 0;
        if ($ql <= $l && $r <= $qr) return $this->tree[$idx];
        $mid = ($l + $r) >> 1;
        return max($this->query($idx * 2, $l, $mid, $ql, $qr), $this->query($idx * 2 + 1, $mid + 1, $r, $ql, $qr));
    }
}
