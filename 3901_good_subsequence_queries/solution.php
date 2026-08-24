<?php
// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

class SegmentTree3901 {
    public $tr;
    function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }
    function __construct($n) {
        $this->tr = [];
        $sz = $n << 2;
        for ($i = 0; $i < $sz; $i++) $this->tr[$i] = ['l' => 0, 'r' => 0, 'g' => 0];
        $this->build(1, 1, $n);
    }
    function build($u, $l, $r) {
        $this->tr[$u]['l'] = $l;
        $this->tr[$u]['r'] = $r;
        $this->tr[$u]['g'] = 0;
        if ($l === $r) return;
        $mid = ($l + $r) >> 1;
        $this->build($u << 1, $l, $mid);
        $this->build($u << 1 | 1, $mid + 1, $r);
    }
    function pushup($u) {
        $this->tr[$u]['g'] = $this->gcd($this->tr[$u << 1]['g'], $this->tr[$u << 1 | 1]['g']);
    }
    function modify($u, $x, $v) {
        if ($this->tr[$u]['l'] === $this->tr[$u]['r']) { $this->tr[$u]['g'] = $v; return; }
        $mid = ($this->tr[$u]['l'] + $this->tr[$u]['r']) >> 1;
        if ($x <= $mid) $this->modify($u << 1, $x, $v);
        else $this->modify($u << 1 | 1, $x, $v);
        $this->pushup($u);
    }
    function query($u, $l, $r) {
        if ($l > $r) return 0;
        if ($this->tr[$u]['l'] >= $l && $this->tr[$u]['r'] <= $r) return $this->tr[$u]['g'];
        $mid = ($this->tr[$u]['l'] + $this->tr[$u]['r']) >> 1;
        if ($r <= $mid) return $this->query($u << 1, $l, $r);
        if ($l > $mid) return $this->query($u << 1 | 1, $l, $r);
        return $this->gcd($this->query($u << 1, $l, $mid), $this->query($u << 1 | 1, $mid + 1, $r));
    }
}

class Solution {
    function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }
    function countGoodSubseq($nums, $p, $queries) {
        $n = count($nums);
        $tree = new SegmentTree3901($n);
        $cnt = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] % $p === 0) {
                $tree->modify(1, $i + 1, $nums[$i]);
                $cnt++;
            }
        }
        $ans = 0;
        foreach ($queries as $q) {
            $idx = $q[0];
            $val = $q[1];
            if ($nums[$idx] % $p === 0) {
                $tree->modify(1, $idx + 1, 0);
                $cnt--;
            }
            if ($val % $p === 0) {
                $tree->modify(1, $idx + 1, $val);
                $cnt++;
            }
            $nums[$idx] = $val;
            if ($tree->tr[1]['g'] !== $p) continue;
            if ($cnt < $n || $n > 6) {
                $ans++;
                continue;
            }
            for ($i = 1; $i <= $n; $i++) {
                $leftG = $tree->query(1, 1, $i - 1);
                $rightG = $tree->query(1, $i + 1, $n);
                if ($this->gcd($leftG, $rightG) === $p) { $ans++; break; }
            }
        }
        return $ans;
    }
}
