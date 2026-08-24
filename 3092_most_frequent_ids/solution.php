<?php
// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

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
    function mostFrequentIDs($nums, $freq) {
        $n = count($nums);
        $cnt = [];
        $lazy = [];
        $ans = array_fill(0, $n, 0);
        $pq = new MinHeap(function ($a, $b) { return $b <=> $a; });
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $f = $freq[$i];
            $old = $cnt[$x] ?? 0;
            $lazy[$old] = ($lazy[$old] ?? 0) + 1;
            $neu = $old + $f;
            $cnt[$x] = $neu;
            $pq->push($neu);
            while ($pq->size() && ($lazy[$pq->peek()] ?? 0) > 0) {
                $top = $pq->pop();
                $lazy[$top]--;
            }
            $ans[$i] = $pq->size() ? $pq->peek() : 0;
        }
        return $ans;
    }
}
