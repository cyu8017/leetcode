<?php
// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

class Hashing {
    public $mod;
    public $p;
    public $h;
    function __construct($word, $bas, $mod) {
        $this->mod = $mod;
        $n = strlen($word);
        $this->p = array_fill(0, $n + 1, 0);
        $this->h = array_fill(0, $n + 1, 0);
        $this->p[0] = 1;
        $this->h[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            $this->p[$i] = ($this->p[$i - 1] * $bas) % $mod;
            $this->h[$i] = ($this->h[$i - 1] * $bas + (ord($word[$i - 1]) - 97)) % $mod;
        }
    }
    function query($l, $r) {
        $M = $this->mod;
        $val = $this->h[$r] - ($this->h[$l - 1] * $this->p[$r - $l + 1] % $M);
        $val %= $M;
        if ($val < 0) $val += $M;
        return $val;
    }
}

class Solution {
    function minimumTimeToInitialState($word, $k) {
        $hashing = new Hashing($word, 13331, 998244353);
        $n = strlen($word);
        for ($i = $k; $i < $n; $i += $k) {
            if ($hashing->query(1, $n - $i) === $hashing->query($i + 1, $n)) return intdiv($i, $k);
        }
        return intdiv($n + $k - 1, $k);
    }
}
