<?php
// LeetCode 3906 - Count Good Integers on a Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

class Solution {
    public $key;
    public $s;
    public $f;
    function dfs($pos, $last, $lim) {
        if ($pos === 16) return 1;
        if (!$lim && $this->f[$pos][$last] !== -1) return $this->f[$pos][$last];
        $res = 0;
        $start = $this->key[$pos] ? $last : 0;
        $end = $lim ? (ord($this->s[$pos]) - 48) : 9;
        for ($i = $start; $i <= $end; $i++) {
            $nextLast = $this->key[$pos] ? $i : $last;
            $res += $this->dfs($pos + 1, $nextLast, $lim && ($i === $end));
        }
        if (!$lim) $this->f[$pos][$last] = $res;
        return $res;
    }
    function calc($x) {
        if ($x < 0) return 0;
        $t = strval($x);
        $this->s = str_repeat('0', 16 - strlen($t)) . $t;
        $this->f = [];
        for ($i = 0; $i < 16; $i++) $this->f[$i] = array_fill(0, 10, -1);
        return $this->dfs(0, 0, true);
    }
    function countGoodIntegersOnPath($l, $r, $directions) {
        $this->key = array_fill(0, 16, false);
        $row = 0;
        $col = 0;
        $this->key[0] = true;
        $n = strlen($directions);
        for ($i = 0; $i < $n; $i++) {
            $c = $directions[$i];
            if ($c === 'D') $row++;
            else $col++;
            $this->key[$row * 4 + $col] = true;
        }
        return $this->calc($r) - $this->calc($l - 1);
    }
}
