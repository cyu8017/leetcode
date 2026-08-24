<?php
// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

class Solution {
    function minimumDistance($n, $edges, $s, $marked) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) $g[$e[0]][] = [$e[1], $e[2]];
        $mark = array_fill_keys($marked, true);
        $INF = 1000000000000;
        $dist = array_fill(0, $n, $INF);
        $dist[$s] = 0;
        $pq = new SplPriorityQueue();
        $pq->insert([$s, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $u = $cur[0];
            $d = $cur[1];
            if (isset($mark[$u])) return $d;
            if ($d > $dist[$u]) continue;
            foreach ($g[$u] as $e) {
                $v = $e[0];
                $w = $e[1];
                if ($d + $w < $dist[$v]) {
                    $dist[$v] = $d + $w;
                    $pq->insert([$v, $dist[$v]], -$dist[$v]);
                }
            }
        }
        return -1;
    }
}
