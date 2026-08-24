<?php
// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

class Solution {
    function modifiedGraphEdges($n, $edges, $source, $destination, $target) {
        $INF = 2000000000;
        $dijkstra = function($ignoreNeg) use ($n, &$edges, $source, $INF) {
            $dist = array_fill(0, $n, $INF);
            $dist[$source] = 0;
            $pq = new SplPriorityQueue();
            $pq->insert([$source, 0], 0);
            while (!$pq->isEmpty()) {
                $cur = $pq->extract();
                $u = $cur[0];
                $d = $cur[1];
                if ($d !== $dist[$u]) continue;
                foreach ($edges as $e) {
                    $a = $e[0];
                    $b = $e[1];
                    $w = $e[2];
                    if ($a !== $u && $b !== $u) continue;
                    $to = $a === $u ? $b : $a;
                    if ($w === -1) {
                        if ($ignoreNeg) continue;
                        $w = 1;
                    }
                    if ($d + $w < $dist[$to]) {
                        $dist[$to] = $d + $w;
                        $pq->insert([$to, $dist[$to]], -$dist[$to]);
                    }
                }
            }
            return $dist;
        };
        $d = $dijkstra(true);
        if ($d[$destination] < $target) return [];
        $matched = $d[$destination] === $target;
        for ($i = 0; $i < count($edges); $i++) {
            if ($edges[$i][2] !== -1) continue;
            if ($matched) {
                $edges[$i][2] = $INF;
                continue;
            }
            $edges[$i][2] = 1;
            $d = $dijkstra(false);
            if ($d[$destination] <= $target) {
                $edges[$i][2] += $target - $d[$destination];
                $matched = true;
            }
        }
        $d = $dijkstra(false);
        if ($d[$destination] !== $target) return [];
        return $edges;
    }
}
