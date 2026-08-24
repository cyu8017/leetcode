<?php
// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

class Solution {
    function minCost($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $w = $e[2];
            $g[$u][] = [$v, $w];
            $g[$v][] = [$u, $w * 2];
        }
        $inf = 1073741823;
        $dist = array_fill(0, $n, $inf);
        $dist[0] = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $d = $cur[0];
            $u = $cur[1];
            if ($d > $dist[$u]) continue;
            if ($u === $n - 1) return $d;
            foreach ($g[$u] as $e) {
                $v = $e[0];
                $w = $e[1];
                $nd = $d + $w;
                if ($nd < $dist[$v]) {
                    $dist[$v] = $nd;
                    $pq->insert([$nd, $v], -$nd);
                }
            }
        }
        return -1;
    }
}
