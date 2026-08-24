<?php
// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

class _LBNode {
    public $l = 0;
    public $r = 0;
    public $mn = 0;
    public $mx = 0;
    public $lazy = 0;
}

class _LBSegTree {
    public $tr;
    function __construct($n) {
        $this->tr = [];
        $sz = $n << 2;
        for ($i = 0; $i <= $sz; $i++) $this->tr[$i] = new _LBNode();
        $this->build(1, 0, $n);
    }
    function build($u, $l, $r) {
        $tr = $this->tr;
        $tr[$u]->l = $l; $tr[$u]->r = $r; $tr[$u]->mn = 0; $tr[$u]->mx = 0; $tr[$u]->lazy = 0;
        if ($l === $r) return;
        $mid = ($l + $r) >> 1;
        $this->build($u << 1, $l, $mid);
        $this->build($u << 1 | 1, $mid + 1, $r);
    }
    function apply($u, $v) {
        $this->tr[$u]->mn += $v;
        $this->tr[$u]->mx += $v;
        $this->tr[$u]->lazy += $v;
    }
    function pushup($u) {
        $tr = $this->tr;
        $tr[$u]->mn = min($tr[$u << 1]->mn, $tr[$u << 1 | 1]->mn);
        $tr[$u]->mx = max($tr[$u << 1]->mx, $tr[$u << 1 | 1]->mx);
    }
    function pushdown($u) {
        if ($this->tr[$u]->lazy !== 0) {
            $v = $this->tr[$u]->lazy;
            $this->apply($u << 1, $v);
            $this->apply($u << 1 | 1, $v);
            $this->tr[$u]->lazy = 0;
        }
    }
    function modify($u, $l, $r, $v) {
        $tr = $this->tr;
        if ($tr[$u]->l >= $l && $tr[$u]->r <= $r) {
            $this->apply($u, $v);
            return;
        }
        $this->pushdown($u);
        $mid = ($tr[$u]->l + $tr[$u]->r) >> 1;
        if ($l <= $mid) $this->modify($u << 1, $l, $r, $v);
        if ($r > $mid) $this->modify($u << 1 | 1, $l, $r, $v);
        $this->pushup($u);
    }
    function query($u, $target) {
        $tr = $this->tr;
        if ($tr[$u]->l === $tr[$u]->r) return $tr[$u]->l;
        $this->pushdown($u);
        $left = $u << 1;
        $right = $u << 1 | 1;
        if ($tr[$left]->mn <= $target && $target <= $tr[$left]->mx) return $this->query($left, $target);
        return $this->query($right, $target);
    }
}

class Solution {
    function longestBalanced($nums) {
        $n = count($nums);
        $st = new _LBSegTree($n);
        $last = [];
        $now = 0;
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            $x = $nums[$i - 1];
            $det = ($x & 1) !== 0 ? 1 : -1;
            if (isset($last[$x])) {
                $st->modify(1, $last[$x], $n, -$det);
                $now -= $det;
            }
            $last[$x] = $i;
            $st->modify(1, $i, $n, $det);
            $now += $det;
            $pos = $st->query(1, $now);
            $ans = max($ans, $i - $pos);
        }
        return $ans;
    }
}
