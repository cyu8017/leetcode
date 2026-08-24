<?php
// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

class Solution {
    public $s;
    public $k;
    public $memo;
    function numberOfBeautifulIntegers($low, $high, $k) {
        $this->k = $k;
        return $this->count($high) - $this->count($low - 1);
    }
    function count($n) {
        if ($n < 0) return 0;
        $this->s = (string)$n;
        $this->memo = [];
        return $this->dfs(0, 0, 0, 1, 0);
    }
    function dfs($pos, $diff, $mod, $tight, $started) {
        if ($pos === strlen($this->s)) return ($started && $diff === 0 && $mod === 0) ? 1 : 0;
        $key = $pos . ',' . $diff . ',' . $mod . ',' . $tight . ',' . $started;
        if (isset($this->memo[$key])) return $this->memo[$key];
        $up = $tight ? ord($this->s[$pos]) - 48 : 9;
        $ans = 0;
        for ($digit = 0; $digit <= $up; $digit++) {
            $nt = ($tight && $digit === $up) ? 1 : 0;
            if (!$started) {
                if ($digit === 0) $ans += $this->dfs($pos + 1, $diff, $mod, $nt, 0);
                else {
                    $nd = $diff + ($digit % 2 === 0 ? 1 : -1);
                    $ans += $this->dfs($pos + 1, $nd, $digit % $this->k, $nt, 1);
                }
            } else {
                $nd = $diff + ($digit % 2 === 0 ? 1 : -1);
                $ans += $this->dfs($pos + 1, $nd, ($mod * 10 + $digit) % $this->k, $nt, 1);
            }
        }
        return $this->memo[$key] = $ans;
    }
}
