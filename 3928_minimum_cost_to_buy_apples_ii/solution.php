<?php
// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

class Solution {
    function minCostToBuyApples($n, $prices, $roads) {
        $g = array_fill(0, $n, []);
        foreach ($roads as $road) {
            $empty = $road[2];
            $full = $road[2] * $road[3];
            $g[$road[0]][] = [$road[1], $empty, $full];
            $g[$road[1]][] = [$road[0], $empty, $full];
        }
        $inf = PHP_INT_MAX / 4;
        $answer = array_fill(0, $n, 0);
        for ($source = 0; $source < $n; $source++) {
            $emptyDist = $this->dijkstra($n, $g, $source, false, $inf);
            $fullDist = $this->dijkstra($n, $g, $source, true, $inf);
            $best = $prices[$source];
            for ($shop = 0; $shop < $n; $shop++) {
                if ($emptyDist[$shop] === $inf || $fullDist[$shop] === $inf) continue;
                $total = $emptyDist[$shop] + $fullDist[$shop] + $prices[$shop];
                if ($total < $best) $best = $total;
            }
            $answer[$source] = $best;
        }
        return $answer;
    }

    private function dijkstra($n, $g, $source, $carrying, $inf) {
        $dist = array_fill(0, $n, $inf);
        $dist[$source] = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([$source, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $node = $cur[0];
            $d = $cur[1];
            if ($d !== $dist[$node]) continue;
            foreach ($g[$node] as $e) {
                $weight = $carrying ? $e[2] : $e[1];
                $next = $d + $weight;
                if ($next < $dist[$e[0]]) {
                    $dist[$e[0]] = $next;
                    $pq->insert([$e[0], $next], -$next);
                }
            }
        }
        return $dist;
    }
}
