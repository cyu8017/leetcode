<?php
// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

class Solution {
    private $g;
    private $inT;
    private $outT;
    private $dist;
    private $parent;
    private $time;
    private $bit;
    private $n;

    private function dfs($u, $p) {
        $this->inT[$u] = $this->time++;
        foreach ($this->g[$u] as $e) {
            $to = $e[0];
            $w = $e[1];
            if ($to === $p) continue;
            $this->parent[$to] = $u;
            $this->dist[$to] = $this->dist[$u] + $w;
            $this->dfs($to, $u);
        }
        $this->outT[$u] = $this->time - 1;
    }

    private function add($i, $v) {
        for (; $i <= $this->n; $i += $i & -$i) $this->bit[$i] += $v;
    }

    private function rangeAdd($l, $r, $v) {
        $this->add($l + 1, $v);
        $this->add($r + 2, -$v);
    }

    private function point($i) {
        $s = 0;
        for ($i++; $i > 0; $i -= $i & -$i) $s += $this->bit[$i];
        return $s;
    }

    function treeQueries($n, $edges, $queries) {
        $this->n = $n;
        $this->g = array_fill(0, $n + 1, []);
        $weight = [];
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $w = $e[2];
            $this->g[$u][] = [$v, $w];
            $this->g[$v][] = [$u, $w];
            $a = min($u, $v);
            $b = max($u, $v);
            $weight[$a . ',' . $b] = $w;
        }
        $this->inT = array_fill(0, $n + 1, 0);
        $this->outT = array_fill(0, $n + 1, 0);
        $this->dist = array_fill(0, $n + 1, 0);
        $this->parent = array_fill(0, $n + 1, 0);
        $this->time = 0;
        $this->dfs(1, 0);
        $this->bit = array_fill(0, $n + 2, 0);
        for ($i = 1; $i <= $n; $i++) $this->rangeAdd($this->inT[$i], $this->inT[$i], $this->dist[$i]);
        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $u = $q[1];
                $v = $q[2];
                $nw = $q[3];
                $a = min($u, $v);
                $b = max($u, $v);
                $key = $a . ',' . $b;
                $ow = $weight[$key];
                $delta = $nw - $ow;
                $weight[$key] = $nw;
                $child = $this->parent[$u] === $v ? $u : $v;
                $this->rangeAdd($this->inT[$child], $this->outT[$child], $delta);
            } else {
                $ans[] = $this->point($this->inT[$q[1]]);
            }
        }
        return $ans;
    }
}
