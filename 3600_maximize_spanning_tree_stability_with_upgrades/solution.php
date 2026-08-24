<?php
// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

class UnionFind3600 {
    public $p;
    public $size;
    public $cnt;

    function __construct($n) {
        $this->p = [];
        $this->size = [];
        $this->cnt = $n;
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
        $this->cnt--;
        return true;
    }
}

class Solution {
    private $n;
    private $edges;
    private $k;

    private function check($lim) {
        $uf = new UnionFind3600($this->n);
        foreach ($this->edges as $e) if ($e[2] >= $lim) $uf->unite($e[0], $e[1]);
        $rem = $this->k;
        foreach ($this->edges as $e) {
            if ($e[2] * 2 >= $lim && $rem > 0) {
                if ($uf->unite($e[0], $e[1])) $rem--;
            }
        }
        return $uf->cnt === 1;
    }

    function maxStability($n, $edges, $k) {
        $this->n = $n;
        $this->edges = $edges;
        $this->k = $k;
        $uf = new UnionFind3600($n);
        $mn = 1000000;
        foreach ($edges as $e) {
            if ($e[3] === 1) {
                $mn = min($mn, $e[2]);
                if (!$uf->unite($e[0], $e[1])) return -1;
            }
        }
        foreach ($edges as $e) $uf->unite($e[0], $e[1]);
        if ($uf->cnt > 1) return -1;
        $l = 1;
        $r = $mn;
        while ($l < $r) {
            $mid = ($l + $r + 1) >> 1;
            if ($this->check($mid)) $l = $mid;
            else $r = $mid - 1;
        }
        return $l;
    }
}
