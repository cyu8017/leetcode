<?php
// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

class Solution {
    public $cnt;
    public $s;
    function findProductsOfElements($queries) {
        $M = 50;
        $this->cnt = array_fill(0, $M + 1, 0);
        $this->s = array_fill(0, $M + 1, 0);
        $p = 1;
        for ($i = 1; $i <= $M; $i++) {
            $this->cnt[$i] = $this->cnt[$i - 1] * 2 + $p;
            $this->s[$i] = $this->s[$i - 1] * 2 + $p * ($i - 1);
            $p *= 2;
        }
        $ans = [];
        for ($i = 0; $i < count($queries); $i++) {
            $left = $queries[$i][0];
            $right = $queries[$i][1];
            $mod = $queries[$i][2];
            $power = $this->f($right + 1) - $this->f($left);
            $ans[$i] = $this->qpow(2, $power, $mod);
        }
        return $ans;
    }
    function numIdxAndSum($x) {
        $idx = 0;
        $totalSum = 0;
        while ($x > 0) {
            $i = 0;
            $t = $x;
            while ($t > 1) { $t >>= 1; $i++; }
            $idx += $this->cnt[$i];
            $totalSum += $this->s[$i];
            $x -= 1 << $i;
            $totalSum += ($x + 1) * $i;
            $idx += $x + 1;
        }
        return [$idx, $totalSum];
    }
    function f($i) {
        $M = 50;
        $l = 0;
        $r = 1 << $M;
        while ($l < $r) {
            $mid = ($l + $r + 1) >> 1;
            $p = $this->numIdxAndSum($mid);
            if ($p[0] < $i) $l = $mid;
            else $r = $mid - 1;
        }
        $p = $this->numIdxAndSum($l);
        $totalSum = $p[1];
        $i -= $p[0];
        $x = $l + 1;
        for ($j = 0; $j < $i; $j++) {
            $y = $x & -$x;
            $tz = 0;
            $yy = $y;
            while (($yy & 1) === 0) { $tz++; $yy >>= 1; }
            $totalSum += $tz;
            $x -= $y;
        }
        return $totalSum;
    }
    function qpow($a, $n, $mod) {
        $ans = 1 % $mod;
        $a %= $mod;
        while ($n > 0) {
            if (($n & 1) !== 0) $ans = $ans * $a % $mod;
            $a = $a * $a % $mod;
            $n >>= 1;
        }
        return $ans;
    }
}
