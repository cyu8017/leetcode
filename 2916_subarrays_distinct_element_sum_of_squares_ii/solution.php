<?php
// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

class Solution {
    private $MOD = 1000000007;
    private $tree;

    function sumCounts($nums) {
        $n = count($nums);
        $this->tree = [];
        for ($i = 0; $i < 4 * ($n + 2); $i++) $this->tree[$i] = ['sum' => 0, 'sumSq' => 0, 'lazy' => 0];
        $last = [];
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            $v = $nums[$i - 1];
            $prev = $last[$v] ?? 0;
            $this->update(1, 1, $n, $prev + 1, $i, 1);
            $ans = ($ans + $this->tree[1]['sumSq']) % $this->MOD;
            $last[$v] = $i;
        }
        return $ans;
    }

    private function apply($idx, $l, $r, $val) {
        $length = $r - $l + 1;
        $this->tree[$idx]['sumSq'] = ($this->tree[$idx]['sumSq'] + 2 * $val % $this->MOD * $this->tree[$idx]['sum'] % $this->MOD
            + $val % $this->MOD * $val % $this->MOD * $length % $this->MOD) % $this->MOD;
        $this->tree[$idx]['sum'] = ($this->tree[$idx]['sum'] + $val % $this->MOD * $length % $this->MOD) % $this->MOD;
        $this->tree[$idx]['lazy'] = ($this->tree[$idx]['lazy'] + $val) % $this->MOD;
    }

    private function update($idx, $l, $r, $ql, $qr, $val) {
        if ($ql > $r || $qr < $l) return;
        if ($ql <= $l && $r <= $qr) {
            $this->apply($idx, $l, $r, $val);
            return;
        }
        if ($this->tree[$idx]['lazy'] !== 0 && $l !== $r) {
            $mid = intdiv($l + $r, 2);
            $this->apply($idx * 2, $l, $mid, $this->tree[$idx]['lazy']);
            $this->apply($idx * 2 + 1, $mid + 1, $r, $this->tree[$idx]['lazy']);
            $this->tree[$idx]['lazy'] = 0;
        }
        $mid = intdiv($l + $r, 2);
        $this->update($idx * 2, $l, $mid, $ql, $qr, $val);
        $this->update($idx * 2 + 1, $mid + 1, $r, $ql, $qr, $val);
        $this->tree[$idx]['sum'] = ($this->tree[$idx * 2]['sum'] + $this->tree[$idx * 2 + 1]['sum']) % $this->MOD;
        $this->tree[$idx]['sumSq'] = ($this->tree[$idx * 2]['sumSq'] + $this->tree[$idx * 2 + 1]['sumSq']) % $this->MOD;
    }
}
