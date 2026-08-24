<?php
// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

class _MinHeap {
    public $a = [];
    public $cmp;
    function __construct($cmp = null) {
        $this->cmp = $cmp ?: function($x, $y) { return $x - $y; };
    }
    function _up($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            if ($cmp($a[$i], $a[$p]) >= 0) break;
            $t = $a[$i]; $a[$i] = $a[$p]; $a[$p] = $t;
            $i = $p;
        }
    }
    function _down($i) {
        $a = &$this->a;
        $cmp = $this->cmp;
        $n = count($a);
        while (true) {
            $s = $i;
            $l = $i * 2 + 1;
            $r = $l + 1;
            if ($l < $n && $cmp($a[$l], $a[$s]) < 0) $s = $l;
            if ($r < $n && $cmp($a[$r], $a[$s]) < 0) $s = $r;
            if ($s === $i) break;
            $t = $a[$i]; $a[$i] = $a[$s]; $a[$s] = $t;
            $i = $s;
        }
    }
    function push($x) { $this->a[] = $x; $this->_up(count($this->a) - 1); }
    function pop() {
        $a = &$this->a;
        if (!count($a)) return null;
        $top = $a[0];
        $last = array_pop($a);
        if (count($a)) { $a[0] = $last; $this->_down(0); }
        return $top;
    }
    function peek() { return $this->a[0]; }
    function size() { return count($this->a); }
}

class Solution {
    function minCostExcludingMax($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0]; $v = $e[1]; $w = $e[2];
            $g[$u][] = [$v, $w];
            $g[$v][] = [$u, $w];
        }
        $INF = PHP_INT_MAX;
        $dist = [];
        for ($i = 0; $i < $n; $i++) $dist[$i] = [$INF, $INF];
        $dist[0][0] = 0;
        $pq = new _MinHeap(function($a, $b) { return $a[0] - $b[0]; });
        $pq->push([0, 0, 0]);
        while ($pq->size()) {
            $cur = $pq->pop();
            $c = $cur[0]; $u = $cur[1]; $used = $cur[2];
            if ($c > $dist[$u][$used]) continue;
            if ($u === $n - 1 && $used === 1) return $c;
            foreach ($g[$u] as $e) {
                $v = $e[0]; $w = $e[1];
                $nxt = $c + $w;
                if ($nxt < $dist[$v][$used]) {
                    $dist[$v][$used] = $nxt;
                    $pq->push([$nxt, $v, $used]);
                }
                if ($used === 0) {
                    $nxt = $c;
                    if ($nxt < $dist[$v][1]) {
                        $dist[$v][1] = $nxt;
                        $pq->push([$nxt, $v, 1]);
                    }
                }
            }
        }
        return $dist[$n - 1][1];
    }
}
