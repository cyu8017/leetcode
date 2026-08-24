<?php
// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

class Fenwick {
    public $bit;
    function __construct($n) {
        $this->bit = array_fill(0, $n + 2, 0);
    }
    function add($i, $v) {
        $len = count($this->bit);
        for (; $i < $len; $i += $i & -$i) $this->bit[$i] += $v;
    }
    function sum($i) {
        $s = 0;
        for (; $i > 0; $i -= $i & -$i) $s += $this->bit[$i];
        return $s;
    }
}

class Solution {
    function kBigIndices($nums, $k) {
        $n = count($nums);
        $uniq = $nums;
        sort($uniq);
        $m = 0;
        for ($i = 0; $i < count($uniq); $i++) {
            if ($i === 0 || $uniq[$i] !== $uniq[$i - 1]) $uniq[$m++] = $uniq[$i];
        }
        $rank = [];
        for ($i = 0; $i < $m; $i++) $rank[$uniq[$i]] = $i + 1;
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $ft = new Fenwick($m);
        for ($i = 0; $i < $n; $i++) {
            $r = $rank[$nums[$i]];
            $left[$i] = $ft->sum($r - 1);
            $ft->add($r, 1);
        }
        $ft = new Fenwick($m);
        for ($i = $n - 1; $i >= 0; $i--) {
            $r = $rank[$nums[$i]];
            $right[$i] = $ft->sum($r - 1);
            $ft->add($r, 1);
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($left[$i] >= $k && $right[$i] >= $k) $ans++;
        }
        return $ans;
    }
}
