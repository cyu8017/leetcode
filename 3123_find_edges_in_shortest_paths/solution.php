<?php
// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

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
    function findAnswer($n, $edges) {
        $g = array_fill(0, $n, []);
        for ($i = 0; $i < count($edges); $i++) {
            $a = $edges[$i][0];
            $b = $edges[$i][1];
            $w = $edges[$i][2];
            $g[$a][] = [$b, $w, $i];
            $g[$b][] = [$a, $w, $i];
        }
        $INF = 1 << 30;
        $dist = array_fill(0, $n, $INF);
        $dist[0] = 0;
        $pq = new MinHeap(function ($a, $b) { return $a[0] <=> $b[0]; });
        $pq->push([0, 0]);
        while ($pq->size()) {
            $cur = $pq->pop();
            $da = $cur[0];
            $a = $cur[1];
            if ($da > $dist[$a]) continue;
            foreach ($g[$a] as $e) {
                $b = $e[0];
                $w = $e[1];
                if ($dist[$b] > $dist[$a] + $w) {
                    $dist[$b] = $dist[$a] + $w;
                    $pq->push([$dist[$b], $b]);
                }
            }
        }
        $ans = array_fill(0, count($edges), false);
        if ($dist[$n - 1] === $INF) return $ans;
        $q = [$n - 1];
        while ($q) {
            $a = array_shift($q);
            foreach ($g[$a] as $e) {
                $b = $e[0];
                $w = $e[1];
                $i = $e[2];
                if ($dist[$a] === $dist[$b] + $w) {
                    $ans[$i] = true;
                    $q[] = $b;
                }
            }
        }
        return $ans;
    }
}
