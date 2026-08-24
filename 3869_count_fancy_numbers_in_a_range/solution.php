<?php
// LeetCode 3869 - Count Fancy Numbers in a Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

class Solution {
    public $num;
    public $n;
    public $f;
    function check($s) {
        if ($s < 100) return $s % 11 !== 0;
        $mid = intdiv($s, 10) % 10;
        $last = $s % 10;
        return $mid > 1 && $mid < $last;
    }
    function dfs($pos, $s, $prev, $st, $lim) {
        if ($pos >= $this->n) {
            if ($st !== 3) return 1;
            return $this->check($s) ? 1 : 0;
        }
        if (!$lim && $this->f[$pos][$s][$prev][$st] !== -1) return $this->f[$pos][$s][$prev][$st];
        $up = $lim ? ord($this->num[$pos]) - 48 : 9;
        $res = 0;
        for ($i = 0; $i <= $up; $i++) {
            $nxtSt = $st;
            if ($st === 0) {
                if ($prev === 0) $nxtSt = 0;
                else if ($i > $prev) $nxtSt = 1;
                else if ($i < $prev) $nxtSt = 2;
                else $nxtSt = 3;
            } else if ($st === 1) {
                $nxtSt = $i > $prev ? 1 : 3;
            } else if ($st === 2) {
                $nxtSt = $i < $prev ? 2 : 3;
            } else {
                $nxtSt = 3;
            }
            $res += $this->dfs($pos + 1, $s + $i, $i, $nxtSt, $lim && $i === $up);
        }
        if (!$lim) $this->f[$pos][$s][$prev][$st] = $res;
        return $res;
    }
    function calc($x) {
        if ($x < 0) return 0;
        $this->num = strval($x);
        $this->n = strlen($this->num);
        $this->f = [];
        for ($i = 0; $i < $this->n; $i++) {
            $this->f[$i] = [];
            for ($s = 0; $s <= 9 * $this->n; $s++) {
                $this->f[$i][$s] = [];
                for ($p = 0; $p < 10; $p++) $this->f[$i][$s][$p] = array_fill(0, 4, -1);
            }
        }
        return $this->dfs(0, 0, 0, 0, true);
    }
    function countFancy($l, $r) {
        return $this->calc($r) - $this->calc($l - 1);
    }
}
