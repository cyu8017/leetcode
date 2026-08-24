<?php
// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

class Solution {
    function minimumWeight($n, $edges, $src1, $src2, $dest) {
        $INF = PHP_INT_MAX / 4;
        $dijkstra = function($g, $src) use ($n, $INF) {
            $dist = array_fill(0, $n, $INF);
            $dist[$src] = 0;
            $pq = new SplPriorityQueue();
            $pq->insert($src, 0);
            while (!$pq->isEmpty()) {
                $u = $pq->extract();
                $d = $dist[$u];
                foreach ($g[$u] as $ew) {
                    $v = $ew[0];
                    $w = $ew[1];
                    if ($d + $w < $dist[$v]) {
                        $dist[$v] = $d + $w;
                        $pq->insert($v, -$dist[$v]);
                    }
                }
            }
            return $dist;
        };
        $g = array_fill(0, $n, []);
        $rg = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $rg[$e[1]][] = [$e[0], $e[2]];
        }
        $d1 = $dijkstra($g, $src1);
        $d2 = $dijkstra($g, $src2);
        $dd = $dijkstra($rg, $dest);
        $ans = $INF;
        for ($i = 0; $i < $n; $i++) {
            if ($d1[$i] >= $INF || $d2[$i] >= $INF || $dd[$i] >= $INF) continue;
            $ans = min($ans, $d1[$i] + $d2[$i] + $dd[$i]);
        }
        return $ans >= $INF ? -1 : $ans;
    }
}
