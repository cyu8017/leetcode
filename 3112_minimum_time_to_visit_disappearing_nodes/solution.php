<?php
// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

class MinHeap {
    public $a = [];
    public $cmp;
    function __construct($cmp = null) {
        $this->cmp = $cmp;
    }
    function _up($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            $c = $cmp ? $cmp($a[$i], $a[$p]) : ($a[$i] <=> $a[$p]);
            if ($c >= 0) break;
            $t = $a[$i]; $a[$i] = $a[$p]; $a[$p] = $t;
            $i = $p;
        }
    }
    function _down($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        $n = count($a);
        while (true) {
            $s = $i; $l = $i * 2 + 1; $r = $l + 1;
            if ($l < $n) {
                $c = $cmp ? $cmp($a[$l], $a[$s]) : ($a[$l] <=> $a[$s]);
                if ($c < 0) $s = $l;
            }
            if ($r < $n) {
                $c = $cmp ? $cmp($a[$r], $a[$s]) : ($a[$r] <=> $a[$s]);
                if ($c < 0) $s = $r;
            }
            if ($s === $i) break;
            $t = $a[$i]; $a[$i] = $a[$s]; $a[$s] = $t;
            $i = $s;
        }
    }
    function push($x) { $this->a[] = $x; $this->_up(count($this->a) - 1); }
    function pop() {
        $a = &$this->a;
        if (!$a) return null;
        $top = $a[0];
        $last = array_pop($a);
        if ($a) { $a[0] = $last; $this->_down(0); }
        return $top;
    }
    function peek() { return $this->a[0]; }
    function size() { return count($this->a); }
}

class Solution {
    function minimumTime($n, $edges, $disappear) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $INF = 1 << 30;
        $dist = array_fill(0, $n, $INF);
        $dist[0] = 0;
        $pq = new MinHeap(function ($a, $b) { return $a[0] <=> $b[0]; });
        $pq->push([0, 0]);
        while ($pq->size()) {
            $cur = $pq->pop();
            $du = $cur[0];
            $u = $cur[1];
            if ($du > $dist[$u]) continue;
            foreach ($g[$u] as $e) {
                $v = $e[0];
                $w = $e[1];
                if ($dist[$v] > $dist[$u] + $w && $dist[$u] + $w < $disappear[$v]) {
                    $dist[$v] = $dist[$u] + $w;
                    $pq->push([$dist[$v], $v]);
                }
            }
        }
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++)
            $ans[$i] = $dist[$i] < $disappear[$i] ? $dist[$i] : -1;
        return $ans;
    }
}
