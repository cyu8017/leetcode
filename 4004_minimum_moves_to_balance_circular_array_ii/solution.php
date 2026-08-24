<?php
// LeetCode 4004 - Minimum Moves to Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

class Solution {
    function minMoves($balance) {
        $totalBalance = 0;
        $totalDeficit = 0;
        foreach ($balance as $x) {
            $totalBalance += $x;
            if ($x < 0) $totalDeficit += -$x;
        }
        if ($totalBalance < 0) return -1;
        if ($totalDeficit === 0) return 0;
        $n = count($balance);
        $source = $n;
        $sink = $n + 1;
        $mcmf = new MinCostMaxFlow($n + 2);
        $INF = 1000000000;
        for ($i = 0; $i < $n; $i++) {
            $x = $balance[$i];
            if ($x > 0) $mcmf->addEdge($source, $i, $x, 0);
            else if ($x < 0) $mcmf->addEdge($i, $sink, -$x, 0);
            $mcmf->addEdge($i, ($i + 1) % $n, $INF, 1);
            $mcmf->addEdge($i, ($i - 1 + $n) % $n, $INF, 1);
        }
        return $mcmf->minCostFlow($source, $sink, $totalDeficit);
    }
}

class MinCostMaxFlow {
    private $n;
    private $graph;
    private $INF = 1000000000;

    function __construct($n_) {
        $this->n = $n_;
        $this->graph = array_fill(0, $n_, []);
    }

    function addEdge($u, $v, $cap, $cost) {
        $this->graph[$u][] = [$v, $cap, $cost, count($this->graph[$v])];
        $this->graph[$v][] = [$u, 0, -$cost, count($this->graph[$u]) - 1];
    }

    function minCostFlow($source, $sink, $maxFlow) {
        $totalCost = 0;
        $currentFlow = 0;
        $n = $this->n;
        while ($currentFlow < $maxFlow) {
            $dist = array_fill(0, $n, $this->INF);
            $parentNode = array_fill(0, $n, -1);
            $parentEdge = array_fill(0, $n, -1);
            $inQueue = array_fill(0, $n, false);
            $q = [$source];
            $dist[$source] = 0;
            $inQueue[$source] = true;
            while (count($q) > 0) {
                $u = array_shift($q);
                $inQueue[$u] = false;
                for ($i = 0; $i < count($this->graph[$u]); $i++) {
                    $e = $this->graph[$u][$i];
                    if ($e[1] > 0 && $dist[$e[0]] > $dist[$u] + $e[2]) {
                        $dist[$e[0]] = $dist[$u] + $e[2];
                        $parentNode[$e[0]] = $u;
                        $parentEdge[$e[0]] = $i;
                        if (!$inQueue[$e[0]]) {
                            $inQueue[$e[0]] = true;
                            $q[] = $e[0];
                        }
                    }
                }
            }
            if ($dist[$sink] === $this->INF) return -1;
            $pushFlow = $maxFlow - $currentFlow;
            for ($cur = $sink; $cur !== $source; $cur = $parentNode[$cur]) {
                $e = $this->graph[$parentNode[$cur]][$parentEdge[$cur]];
                if ($e[1] < $pushFlow) $pushFlow = $e[1];
            }
            for ($cur = $sink; $cur !== $source; $cur = $parentNode[$cur]) {
                $p = $parentNode[$cur];
                $idx = $parentEdge[$cur];
                $rev = $this->graph[$p][$idx][3];
                $this->graph[$p][$idx][1] -= $pushFlow;
                $this->graph[$cur][$rev][1] += $pushFlow;
            }
            $currentFlow += $pushFlow;
            $totalCost += $pushFlow * $dist[$sink];
        }
        return $totalCost;
    }
}
