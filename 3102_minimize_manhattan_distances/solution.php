<?php
// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

class MultiSet {
    public $m = [];
    public $keys = [];
    function merge($x, $v) {
        $nv = ($this->m[$x] ?? 0) + $v;
        if ($nv === 0) {
            unset($this->m[$x]);
            $i = array_search($x, $this->keys, true);
            if ($i !== false) array_splice($this->keys, $i, 1);
        } else {
            if (!isset($this->m[$x])) {
                $lo = 0;
                $hi = count($this->keys);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($this->keys[$mid] < $x) $lo = $mid + 1;
                    else $hi = $mid;
                }
                array_splice($this->keys, $lo, 0, [$x]);
            }
            $this->m[$x] = $nv;
        }
    }
    function first() { return $this->keys[0]; }
    function last() { return $this->keys[count($this->keys) - 1]; }
}

class Solution {
    function minimumDistance($points) {
        $st1 = new MultiSet();
        $st2 = new MultiSet();
        foreach ($points as $p) {
            $st1->merge($p[0] + $p[1], 1);
            $st2->merge($p[0] - $p[1], 1);
        }
        $ans = PHP_INT_MAX;
        foreach ($points as $p) {
            $x = $p[0];
            $y = $p[1];
            $st1->merge($x + $y, -1);
            $st2->merge($x - $y, -1);
            $ans = min($ans, max($st1->last() - $st1->first(), $st2->last() - $st2->first()));
            $st1->merge($x + $y, 1);
            $st2->merge($x - $y, 1);
        }
        return $ans;
    }
}
