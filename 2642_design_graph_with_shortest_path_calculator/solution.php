<?php
// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph {
    private $g;

    function __construct($n, $edges) {
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) $this->g[$e[0]][] = [$e[1], $e[2]];
    }

    function addEdge($edge) {
        $this->g[$edge[0]][] = [$edge[1], $edge[2]];
    }

    function shortestPath($node1, $node2) {
        $n = count($this->g);
        $dist = array_fill(0, $n, 1 << 30);
        $dist[$node1] = 0;
        $pq = new SplPriorityQueue();
        $pq->insert([$node1, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $u = $cur[0];
            $d = $cur[1];
            if ($u === $node2) return $d;
            if ($d > $dist[$u]) continue;
            foreach ($this->g[$u] as $e) {
                $v = $e[0];
                $w = $e[1];
                $nd = $d + $w;
                if ($nd < $dist[$v]) {
                    $dist[$v] = $nd;
                    $pq->insert([$v, $nd], -$nd);
                }
            }
        }
        return -1;
    }
}
