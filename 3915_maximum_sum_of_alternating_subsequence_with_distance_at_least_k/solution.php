<?php
// LeetCode 3915 - Maximum Sum of Alternating Subsequence With Distance at Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

class Fenwick3915 {
    public $f;
    function __construct($n) {
        $this->f = array_fill(0, $n, 0);
    }
    function update($i, $val) {
        for (; $i < count($this->f); $i += $i & -$i) $this->f[$i] = max($this->f[$i], $val);
    }
    function preMax($i) {
        $res = 0;
        for (; $i > 0; $i &= $i - 1) $res = max($res, $this->f[$i]);
        return $res;
    }
}

class Solution {
    function maxAlternatingSum($nums, $k) {
        $sorted = $nums;
        sort($sorted);
        $m = 0;
        $uniq = [];
        for ($i = 0; $i < count($sorted); $i++) {
            if ($i === 0 || $sorted[$i] !== $sorted[$i - 1]) $uniq[$m++] = $sorted[$i];
        }
        $sorted = $uniq;
        $n = count($nums);
        $fInc = array_fill(0, $n, 0);
        $fDec = array_fill(0, $n, 0);
        $inc = new Fenwick3915($m + 1);
        $dec = new Fenwick3915($m + 1);
        $ans = 0;
        $ranks = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($i >= $k) {
                $j = $ranks[$i - $k];
                $inc->update($m - $j, $fInc[$i - $k]);
                $dec->update($j + 1, $fDec[$i - $k]);
            }
            $lo = 0;
            $hi = count($sorted);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($sorted[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            $ranks[$i] = $lo;
            $fInc[$i] = $dec->preMax($lo) + $x;
            $fDec[$i] = $inc->preMax($m - 1 - $lo) + $x;
            $ans = max($ans, max($fInc[$i], $fDec[$i]));
        }
        return $ans;
    }
}
