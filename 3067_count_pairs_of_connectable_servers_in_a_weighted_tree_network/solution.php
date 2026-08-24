<?php
// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

class Solution {
    public $g;
    public $signalSpeed;
    function countPairsOfConnectableServers($edges, $signalSpeed) {
        $n = count($edges) + 1;
        $this->signalSpeed = $signalSpeed;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = [$e[1], $e[2]];
            $this->g[$e[1]][] = [$e[0], $e[2]];
        }
        $ans = array_fill(0, $n, 0);
        for ($a = 0; $a < $n; $a++) {
            $s = 0;
            foreach ($this->g[$a] as $e) {
                $t = $this->dfs($e[0], $a, $e[1]);
                $ans[$a] += $s * $t;
                $s += $t;
            }
        }
        return $ans;
    }
    function dfs($a, $fa, $ws) {
        $cnt = $ws % $this->signalSpeed === 0 ? 1 : 0;
        foreach ($this->g[$a] as $e) {
            if ($e[0] !== $fa) $cnt += $this->dfs($e[0], $a, $ws + $e[1]);
        }
        return $cnt;
    }
}
