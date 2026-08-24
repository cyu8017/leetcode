<?php
// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

class FenwickMax {
    public $vals;
    function __construct($n) {
        $this->vals = array_fill(0, $n + 1, 0);
    }
    function maximize($i, $val) {
        for (; $i < count($this->vals); $i += $i & -$i)
            $this->vals[$i] = max($this->vals[$i], $val);
    }
    function get($i) {
        $res = 0;
        for (; $i > 0; $i -= $i & -$i) $res = max($res, $this->vals[$i]);
        return $res;
    }
}

class Solution {
    function getResults($queries) {
        $n = count($queries) * 3;
        if ($n > 50000) $n = 50000;
        $tree = new FenwickMax($n + 1);
        $obs = [0, $n];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $x = $q[1];
                $idx = $this->lowerBound($obs, $x);
                if ($idx === count($obs) || $obs[$idx] !== $x) array_splice($obs, $idx, 0, [$x]);
            }
        }
        for ($i = 0; $i + 1 < count($obs); $i++) {
            $tree->maximize($obs[$i + 1], $obs[$i + 1] - $obs[$i]);
        }
        $ans = [];
        for ($i = count($queries) - 1; $i >= 0; $i--) {
            $typ = $queries[$i][0];
            $x = $queries[$i][1];
            if ($typ === 1) {
                $j = $this->lowerBound($obs, $x);
                $prev = $obs[$j - 1];
                $next = $obs[$j + 1];
                array_splice($obs, $j, 1);
                $tree->maximize($next, $next - $prev);
            } else {
                $sz = $queries[$i][2];
                $j = $this->lowerBound($obs, $x + 1) - 1;
                $prev = $obs[$j];
                $ans[] = $tree->get($prev) >= $sz || $x - $prev >= $sz;
            }
        }
        return array_reverse($ans);
    }
    function lowerBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
