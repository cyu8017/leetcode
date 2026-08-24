<?php
// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

class UnionFind3608 {
    public $p;
    public $size;

    function __construct($n) {
        $this->p = [];
        $this->size = [];
        for ($i = 0; $i < $n; $i++) { $this->p[$i] = $i; $this->size[$i] = 1; }
    }

    function find($x) {
        if ($this->p[$x] !== $x) $this->p[$x] = $this->find($this->p[$x]);
        return $this->p[$x];
    }

    function unite($a, $b) {
        $pa = $this->find($a);
        $pb = $this->find($b);
        if ($pa === $pb) return false;
        if ($this->size[$pa] > $this->size[$pb]) {
            $this->p[$pb] = $pa;
            $this->size[$pa] += $this->size[$pb];
        } else {
            $this->p[$pa] = $pb;
            $this->size[$pb] += $this->size[$pa];
        }
        return true;
    }
}

class Solution {
    function minTime($n, $edges, $k) {
        usort($edges, function($a, $b) { return $a[2] <=> $b[2]; });
        $uf = new UnionFind3608($n);
        $cnt = $n;
        for ($i = count($edges) - 1; $i >= 0; $i--) {
            if ($uf->unite($edges[$i][0], $edges[$i][1])) {
                $cnt--;
                if ($cnt < $k) return $edges[$i][2];
            }
        }
        return 0;
    }
}
