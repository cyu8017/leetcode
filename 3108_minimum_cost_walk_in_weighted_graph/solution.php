<?php
// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

class Solution {
    public $p;
    public $size;
    function minimumCost($n, $edges, $query) {
        $this->p = range(0, $n - 1);
        $this->size = array_fill(0, $n, 1);
        $g = array_fill(0, $n, -1);
        foreach ($edges as $e) $this->unite($e[0], $e[1]);
        foreach ($edges as $e) {
            $root = $this->find($e[0]);
            $g[$root] &= $e[2];
        }
        $ans = [];
        for ($i = 0; $i < count($query); $i++) {
            $u = $query[$i][0];
            $v = $query[$i][1];
            if ($u === $v) $ans[$i] = 0;
            else {
                $a = $this->find($u);
                $b = $this->find($v);
                $ans[$i] = $a === $b ? $g[$a] : -1;
            }
        }
        return $ans;
    }
    function find($x) {
        if ($this->p[$x] !== $x) $this->p[$x] = $this->find($this->p[$x]);
        return $this->p[$x];
    }
    function unite($a, $b) {
        $pa = $this->find($a);
        $pb = $this->find($b);
        if ($pa === $pb) return;
        if ($this->size[$pa] > $this->size[$pb]) {
            $this->p[$pb] = $pa;
            $this->size[$pa] += $this->size[$pb];
        } else {
            $this->p[$pa] = $pb;
            $this->size[$pb] += $this->size[$pa];
        }
    }
}
