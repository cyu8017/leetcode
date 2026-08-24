<?php
// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

class Solution {
    private $num;
    private $f;

    private function dfs($pos, $mask, $limit) {
        if ($pos >= strlen($this->num)) return $mask !== 0 ? 1 : 0;
        if (!$limit && $this->f[$pos][$mask] !== -1) return $this->f[$pos][$mask];
        $up = $limit ? ord($this->num[$pos]) - 48 : 9;
        $ans = 0;
        for ($i = 0; $i <= $up; $i++) {
            if ((($mask >> $i) & 1) !== 0) continue;
            $nxt = $mask | (1 << $i);
            if ($mask === 0 && $i === 0) $nxt = 0;
            $ans += $this->dfs($pos + 1, $nxt, $limit && $i === $up);
        }
        if (!$limit) $this->f[$pos][$mask] = $ans;
        return $ans;
    }

    private function reset() {
        $len = strlen($this->num);
        $this->f = [];
        for ($i = 0; $i < $len; $i++) $this->f[$i] = array_fill(0, 1 << 10, -1);
    }

    function numberCount($a, $b) {
        $this->num = (string)$b;
        $this->reset();
        $y = $this->dfs(0, 0, true);
        $this->num = (string)($a - 1);
        $this->reset();
        $x = $this->dfs(0, 0, true);
        return $y - $x;
    }
}
