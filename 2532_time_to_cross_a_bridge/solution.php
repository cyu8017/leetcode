<?php
// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

class _Heap2532 {
    public $a = [];
    public $cmp;
    function __construct($cmp) { $this->cmp = $cmp; }
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
    function findCrossingTime($n, $k, $time) {
        $cmpW = function($a, $b) {
            if ($a['efficiency'] !== $b['efficiency']) return $b['efficiency'] - $a['efficiency'];
            return $b['idx'] - $a['idx'];
        };
        $left = new _Heap2532($cmpW);
        $right = new _Heap2532($cmpW);
        $ws = [];
        for ($i = 0; $i < $k; $i++) {
            $t = $time[$i];
            $ws[$i] = [
                'idx' => $i,
                'leftToRight' => $t[0],
                'pickOld' => $t[1],
                'rightToLeft' => $t[2],
                'putNew' => $t[3],
                'efficiency' => $t[0] + $t[2],
            ];
            $left->push($ws[$i]);
        }
        $events = new _Heap2532(function($a, $b) { return $a[0] - $b[0]; });
        $cur = 0;
        $bridgeFree = 0;
        $remain = $n;
        $done = 0;
        while ($done < $n) {
            while ($events->size() && $events->peek()[0] <= $cur) {
                $e = $events->pop();
                $w = $ws[$e[2]];
                if ($e[1] === 0) $left->push($w);
                else $right->push($w);
            }
            if ($cur < $bridgeFree) {
                $cur = $bridgeFree;
                continue;
            }
            if ($right->size()) {
                $w = $right->pop();
                $cur += $w['rightToLeft'];
                $bridgeFree = $cur;
                $events->push([$cur + $w['putNew'], 0, $w['idx']]);
                $done++;
                continue;
            }
            if ($left->size() && $remain > 0) {
                $w = $left->pop();
                $cur += $w['leftToRight'];
                $bridgeFree = $cur;
                $remain--;
                $events->push([$cur + $w['pickOld'], 1, $w['idx']]);
                continue;
            }
            if (!$events->size()) break;
            $cur = $events->peek()[0];
        }
        return $cur;
    }
}
