<?php
// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

class Solution {
    public $coins;
    public $k;
    public $n;
    function findKthSmallest($coins, $k) {
        $this->coins = $coins;
        $this->k = $k;
        $this->n = count($coins);
        $lo = 1;
        $hi = 100000000000;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($this->check($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
    function gcdll($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }
    function lcmll($a, $b) {
        return intdiv($a, $this->gcdll($a, $b)) * $b;
    }
    function bitCount($x) {
        $c = 0;
        while ($x !== 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }
    function check($mx) {
        $cnt = 0;
        $n = $this->n;
        for ($i = 1; $i < (1 << $n); $i++) {
            $v = 1;
            for ($j = 0; $j < $n; $j++) {
                if ((($i >> $j) & 1) !== 0) {
                    $v = $this->lcmll($v, $this->coins[$j]);
                    if ($v > $mx) break;
                }
            }
            $m = $this->bitCount($i);
            if ($m % 2 === 1) $cnt += intdiv($mx, $v);
            else $cnt -= intdiv($mx, $v);
        }
        return $cnt >= $this->k;
    }
}
