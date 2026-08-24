<?php
// LeetCode 3864 - Minimum Cost to Partition a Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

class Solution {
    public $pre;
    public $encCost;
    public $flatCost;
    function dfs($l, $r) {
        $x = $this->pre[$r] - $this->pre[$l];
        $res = $x !== 0 ? ($r - $l) * $x * $this->encCost : $this->flatCost;
        if (($r - $l) % 2 === 0) {
            $m = intdiv($l + $r, 2);
            $res = min($res, $this->dfs($l, $m) + $this->dfs($m, $r));
        }
        return $res;
    }
    function minCost($s, $encCost, $flatCost) {
        $n = strlen($s);
        $this->encCost = $encCost;
        $this->flatCost = $flatCost;
        $this->pre = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) $this->pre[$i] = $this->pre[$i - 1] + (ord($s[$i - 1]) - 48);
        return $this->dfs(0, $n);
    }
}
