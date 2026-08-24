<?php
// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

class Solution {
    private $MOD = 1000000007;
    private $g;
    private $vals;
    private $ans;

    private function digitMask($x) {
        $v = $x;
        $mask = 0;
        if ($x === 0) return [1, 1, 0];
        while ($x > 0) {
            $d = $x % 10;
            if (($mask & (1 << $d)) !== 0) return [0, 0, 0];
            $mask |= 1 << $d;
            $x = intdiv($x, 10);
        }
        return [$mask, 1, $v];
    }

    private function dfs($u) {
        $dp = [0 => 0];
        $dm = $this->digitMask($this->vals[$u]);
        if ($dm[1] === 1) $dp[$dm[0]] = $dm[2];
        foreach ($this->g[$u] as $c) {
            $child = $this->dfs($c);
            $ndp = [];
            foreach ($dp as $k1 => $v1) {
                foreach ($child as $k2 => $v2) {
                    if (($k1 & $k2) === 0) {
                        $nm = $k1 | $k2;
                        $ndp[$nm] = max($ndp[$nm] ?? 0, $v1 + $v2);
                    }
                }
            }
            foreach ($dp as $k => $v) $ndp[$k] = max($ndp[$k] ?? 0, $v);
            foreach ($child as $k => $v) $ndp[$k] = max($ndp[$k] ?? 0, $v);
            $dp = $ndp;
        }
        $best = 0;
        foreach ($dp as $s) $best = max($best, $s);
        $this->ans = ($this->ans + $best) % $this->MOD;
        return $dp;
    }

    function goodSubtreeSum($vals, $par) {
        $n = count($vals);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->g[$par[$i]][] = $i;
        $this->vals = $vals;
        $this->ans = 0;
        $this->dfs(0);
        return $this->ans;
    }
}
