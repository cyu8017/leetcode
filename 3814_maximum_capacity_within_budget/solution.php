<?php
// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

class _MCHeap {
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
    function maxCapacity($costs, $capacity, $budget) {
        $arr = [];
        for ($k = 0; $k < count($costs); $k++) {
            if ($costs[$k] < $budget) $arr[] = [$costs[$k], $capacity[$k]];
        }
        if (!count($arr)) return 0;
        usort($arr, function($a, $b) { return $a[0] <=> $b[0]; });
        $m = count($arr);
        $alive = array_fill(0, $m, true);
        $h = new _MCHeap(function($a, $b) {
            if ($a[0] !== $b[0]) return $b[0] - $a[0];
            return $b[1] - $a[1];
        });
        for ($i = 0; $i < $m; $i++) $h->push([$arr[$i][1], $i]);
        while ($h->size() && !$alive[$h->peek()[1]]) $h->pop();
        $ans = $h->peek()[0];
        $i = 0;
        $j = $m - 1;
        while ($i < $j) {
            $alive[$i] = false;
            while ($i < $j && $arr[$i][0] + $arr[$j][0] >= $budget) {
                $alive[$j] = false;
                $j--;
            }
            while ($h->size() && !$alive[$h->peek()[1]]) $h->pop();
            if ($h->size()) $ans = max($ans, $arr[$i][1] + $h->peek()[0]);
            $i++;
        }
        return $ans;
    }
}
