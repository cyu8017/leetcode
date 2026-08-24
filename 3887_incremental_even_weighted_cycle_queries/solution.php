<?php
// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

class Solution {
    public $parent;
    public $parity;
    function find($x) {
        if ($this->parent[$x] === $x) return [$x, 0];
        $res = $this->find($this->parent[$x]);
        $root = $res[0];
        $p = $res[1];
        $this->parity[$x] ^= $p;
        $this->parent[$x] = $root;
        return [$root, $this->parity[$x]];
    }
    function countValidEdges($n, $edges) {
        $this->parent = [];
        $size = [];
        $this->parity = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) { $this->parent[$i] = $i; $size[$i] = 1; }
        $ans = 0;
        foreach ($edges as $e) {
            $fu = $this->find($e[0]);
            $fv = $this->find($e[1]);
            $ru = $fu[0];
            $pu = $fu[1];
            $rv = $fv[0];
            $pv = $fv[1];
            if ($ru === $rv) {
                if (($pu ^ $pv) === $e[2]) $ans++;
                continue;
            }
            if ($size[$ru] < $size[$rv]) {
                $t = $ru; $ru = $rv; $rv = $t;
                $t = $pu; $pu = $pv; $pv = $t;
            }
            $this->parent[$rv] = $ru;
            $this->parity[$rv] = $pu ^ $pv ^ $e[2];
            $size[$ru] += $size[$rv];
            $ans++;
        }
        return $ans;
    }
}
