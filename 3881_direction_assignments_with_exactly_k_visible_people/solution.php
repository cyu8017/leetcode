<?php
// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

class Solution {
    public $fact;
    public $invFact;
    public $ready = false;
    const N = 100001;
    const MOD = 1000000007;
    function qmi($a, $k, $p) {
        $res = 1;
        while ($k !== 0) {
            if (($k & 1) !== 0) $res = $res * $a % $p;
            $k >>= 1;
            $a = $a * $a % $p;
        }
        return $res;
    }
    function init() {
        if ($this->ready) return;
        $this->fact = array_fill(0, self::N, 0);
        $this->invFact = array_fill(0, self::N, 0);
        $this->fact[0] = $this->invFact[0] = 1;
        for ($i = 1; $i < self::N; $i++) {
            $this->fact[$i] = $this->fact[$i - 1] * $i % self::MOD;
            $this->invFact[$i] = $this->qmi($this->fact[$i], self::MOD - 2, self::MOD);
        }
        $this->ready = true;
    }
    function comb($n, $k) {
        return $this->fact[$n] * $this->invFact[$k] % self::MOD * $this->invFact[$n - $k] % self::MOD;
    }
    function countVisiblePeople($n, $pos, $k) {
        $this->init();
        $l = $pos;
        $r = $n - $pos - 1;
        $ans = 0;
        $lim = min($k, $l);
        for ($a = 0; $a <= $lim; $a++) {
            $b = $k - $a;
            if ($b <= $r) {
                $ans = ($ans + 2 * $this->comb($l, $a) % self::MOD * $this->comb($r, $b) % self::MOD) % self::MOD;
            }
        }
        return $ans;
    }
}
