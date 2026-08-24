<?php
// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

class Solution {
    private $num;
    private $x;
    private $f;

    private function dfs($pos, $cnt, $limit) {
        if ($pos === 0) return $cnt;
        if (!$limit && $this->f[$pos][$cnt] !== -1) return $this->f[$pos][$cnt];
        $ans = 0;
        $up = $limit ? (($this->num >> ($pos - 1)) & 1) : 1;
        for ($i = 0; $i <= $up; $i++) {
            $v = $cnt;
            if ($i === 1 && $pos % $this->x === 0) $v++;
            $ans += $this->dfs($pos - 1, $v, $limit && $i === $up);
        }
        if (!$limit) $this->f[$pos][$cnt] = $ans;
        return $ans;
    }

    function findMaximumNumber($k, $x) {
        $this->x = $x;
        $l = 1;
        $r = 10 ** 17;
        while ($l < $r) {
            $mid = ($l + $r + 1) >> 1;
            $this->num = $mid;
            $m = 0;
            for ($t = $this->num; $t > 0; $t >>= 1) $m++;
            $this->f = [];
            for ($i = 0; $i < 65; $i++) $this->f[$i] = array_fill(0, 65, -1);
            if ($this->dfs($m, 0, true) <= $k) $l = $mid;
            else $r = $mid - 1;
        }
        return $l;
    }
}
