<?php
// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

class Solution {
    public $s;
    public $k;
    public $red;
    public $memo;
    public $mod;

    function bitsPop($x) {
        $c = 0;
        while ($x > 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    function dfs($pos, $tight, $ones) {
        if ($pos === strlen($this->s)) {
            if ($ones === 0) return 0;
            return $this->red[$ones] <= $this->k - 1 ? 1 : 0;
        }
        $ky = $pos . ',' . ($tight ? 1 : 0) . ',' . $ones;
        if (isset($this->memo[$ky])) return $this->memo[$ky];
        $up = $tight ? (ord($this->s[$pos]) - 48) : 1;
        $ans = 0;
        for ($d = 0; $d <= $up; $d++) {
            $nt = $tight && $d === $up;
            $ans = ($ans + $this->dfs($pos + 1, $nt, $ones + $d)) % $this->mod;
        }
        return $this->memo[$ky] = $ans;
    }

    function countKReducibleNumbers($s, $k) {
        $this->mod = 1000000007;
        $this->s = $s;
        $this->k = $k;
        $this->red = [];
        $this->red[1] = 0;
        for ($i = 2; $i <= 800; $i++) $this->red[$i] = 1 + $this->red[$this->bitsPop($i)];
        $this->memo = [];
        return $this->dfs(0, true, 0);
    }
}
