<?php
// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

class SegNode {
    public $l = 0;
    public $r = 0;
    public $s00 = 0;
    public $s01 = 0;
    public $s10 = 0;
    public $s11 = 0;
}

class Solution {
    public $tr;
    function maximumSumSubsequence($nums, $queries) {
        $n = count($nums);
        $this->tr = [];
        for ($i = 0; $i < $n * 4; $i++) $this->tr[] = new SegNode();
        $this->build(1, 1, $n);
        for ($i = 0; $i < $n; $i++) $this->modify(1, $i + 1, $nums[$i]);
        $MOD = 1000000007;
        $ans = 0;
        foreach ($queries as $q) {
            $this->modify(1, $q[0] + 1, $q[1]);
            $ans = ($ans + $this->query(1, 1, $n)) % $MOD;
        }
        return $ans;
    }
    function build($u, $l, $r) {
        $this->tr[$u]->l = $l;
        $this->tr[$u]->r = $r;
        if ($l === $r) return;
        $mid = ($l + $r) >> 1;
        $this->build($u << 1, $l, $mid);
        $this->build($u << 1 | 1, $mid + 1, $r);
    }
    function pushup($u) {
        $left = $this->tr[$u << 1];
        $right = $this->tr[$u << 1 | 1];
        $this->tr[$u]->s00 = max($left->s00 + $right->s10, $left->s01 + $right->s00);
        $this->tr[$u]->s01 = max($left->s00 + $right->s11, $left->s01 + $right->s01);
        $this->tr[$u]->s10 = max($left->s10 + $right->s10, $left->s11 + $right->s00);
        $this->tr[$u]->s11 = max($left->s10 + $right->s11, $left->s11 + $right->s01);
    }
    function modify($u, $x, $v) {
        if ($this->tr[$u]->l === $this->tr[$u]->r) {
            $this->tr[$u]->s11 = max(0, $v);
            return;
        }
        $mid = ($this->tr[$u]->l + $this->tr[$u]->r) >> 1;
        if ($x <= $mid) $this->modify($u << 1, $x, $v);
        else $this->modify($u << 1 | 1, $x, $v);
        $this->pushup($u);
    }
    function query($u, $l, $r) {
        if ($this->tr[$u]->l >= $l && $this->tr[$u]->r <= $r) return $this->tr[$u]->s11;
        $mid = ($this->tr[$u]->l + $this->tr[$u]->r) >> 1;
        $ans = 0;
        if ($r <= $mid) $ans = $this->query($u << 1, $l, $r);
        if ($l > $mid) $ans = max($ans, $this->query($u << 1 | 1, $l, $r));
        return $ans;
    }
}
