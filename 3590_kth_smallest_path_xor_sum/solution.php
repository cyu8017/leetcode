<?php
// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

class Solution {
    private $g;
    private $vals;
    private $xorPath;
    private $inT;
    private $outT;
    private $order;

    private function dfs($u) {
        $this->xorPath[$u] ^= $this->vals[$u];
        foreach ($this->g[$u] as $v) {
            $this->xorPath[$v] = $this->xorPath[$u];
            $this->dfs($v);
        }
    }

    private function dfs2($u) {
        $this->inT[$u] = count($this->order);
        $this->order[] = $this->xorPath[$u];
        foreach ($this->g[$u] as $v) $this->dfs2($v);
        $this->outT[$u] = count($this->order);
    }

    function kthSmallest($par, $vals, $queries) {
        $n = count($par);
        $this->g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $this->g[$par[$i]][] = $i;
        $this->vals = $vals;
        $this->xorPath = array_fill(0, $n, 0);
        $this->dfs(0);
        $this->inT = array_fill(0, $n, 0);
        $this->outT = array_fill(0, $n, 0);
        $this->order = [];
        $this->dfs2(0);
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $u = $queries[$i][0];
            $k = $queries[$i][1];
            $sub = array_slice($this->order, $this->inT[$u], $this->outT[$u] - $this->inT[$u]);
            sort($sub);
            $uniq = [];
            foreach ($sub as $x) if (count($uniq) === 0 || $uniq[count($uniq) - 1] !== $x) $uniq[] = $x;
            $ans[$i] = $k > count($uniq) ? -1 : $uniq[$k - 1];
        }
        return $ans;
    }
}
