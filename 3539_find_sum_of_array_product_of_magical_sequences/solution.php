<?php
// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

class Solution {
    private $N = 31;
    private $MOD = 1000000007;
    private $f;
    private $g;
    private $nums;
    private $n;
    private $dp;

    private function qpow($a, $kk) {
        $res = 1;
        $mod = $this->MOD;
        $a %= $mod;
        while ($kk > 0) {
            if ($kk & 1) $res = (int)(($res * $a) % $mod);
            $a = (int)(($a * $a) % $mod);
            $kk >>= 1;
        }
        return $res;
    }

    private function initFact() {
        $this->f = array_fill(0, $this->N, 0);
        $this->g = array_fill(0, $this->N, 0);
        $this->f[0] = $this->g[0] = 1;
        for ($i = 1; $i < $this->N; $i++) {
            $this->f[$i] = (int)(($this->f[$i - 1] * $i) % $this->MOD);
            $this->g[$i] = $this->qpow($this->f[$i], $this->MOD - 2);
        }
    }

    private function comb($mm, $nn) {
        if ($nn < 0 || $nn > $mm) return 0;
        return (int)(($this->f[$mm] * $this->g[$nn] % $this->MOD) * $this->g[$mm - $nn] % $this->MOD);
    }

    private function dfs($i, $j, $kk, $st) {
        if ($kk < 0 || ($i === $this->n && $j > 0)) return 0;
        if ($i === $this->n) {
            while ($st > 0) { $kk -= $st & 1; $st >>= 1; }
            return $kk === 0 ? 1 : 0;
        }
        if ($this->dp[$i][$j][$kk][$st] !== -1) return $this->dp[$i][$j][$kk][$st];
        $res = 0;
        for ($t = 0; $t <= $j; $t++) {
            $nt = $t + $st;
            $nk = $kk - ($nt & 1);
            $p = $this->qpow($this->nums[$i], $t);
            $tmp = (int)(($this->comb($j, $t) * $p % $this->MOD) * $this->dfs($i + 1, $j - $t, $nk, $nt >> 1) % $this->MOD);
            $res = ($res + $tmp) % $this->MOD;
        }
        return $this->dp[$i][$j][$kk][$st] = $res;
    }

    function magicalSum($m, $k, $nums) {
        $this->initFact();
        $this->nums = $nums;
        $this->n = count($nums);
        $this->dp = [];
        for ($i = 0; $i <= $this->n; $i++) {
            $this->dp[$i] = [];
            for ($j = 0; $j <= $m; $j++) {
                $this->dp[$i][$j] = [];
                for ($kk = 0; $kk <= $k; $kk++)
                    $this->dp[$i][$j][$kk] = array_fill(0, $this->N, -1);
            }
        }
        return $this->dfs(0, $m, $k, 0);
    }
}
