<?php
// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

class Solution {
    function shortestPathWithHops($n, $edges, $s, $d, $k) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $INF = PHP_INT_MAX >> 2;
        $dist = [];
        for ($i = 0; $i < $n; $i++) $dist[$i] = array_fill(0, $k + 1, $INF);
        $dist[$s][0] = 0;
        $pq = new SplPriorityQueue();
        $pq->insert([$s, 0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $u = $cur[0];
            $hops = $cur[1];
            $cd = $cur[2];
            if ($u === $d) return $cd;
            if ($cd > $dist[$u][$hops]) continue;
            foreach ($g[$u] as $e) {
                $to = $e[0];
                $w = $e[1];
                if ($cd + $w < $dist[$to][$hops]) {
                    $dist[$to][$hops] = $cd + $w;
                    $pq->insert([$to, $hops, $dist[$to][$hops]], -$dist[$to][$hops]);
                }
                if ($hops < $k && $cd < $dist[$to][$hops + 1]) {
                    $dist[$to][$hops + 1] = $cd;
                    $pq->insert([$to, $hops + 1, $cd], -$cd);
                }
            }
        }
        return -1;
    }
}
