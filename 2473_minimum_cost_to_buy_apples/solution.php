<?php
// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

class Solution {
    function minCost($n, $roads, $appleCost, $k) {
        $g = array_fill(0, $n + 1, []);
        foreach ($roads as $r) {
            $g[$r[0]][] = [$r[1], $r[2]];
            $g[$r[1]][] = [$r[0], $r[2]];
        }
        $ans = array_fill(0, $n, 0);
        $INF = intdiv(PHP_INT_MAX, 4);
        for ($start = 1; $start <= $n; $start++) {
            $dist = array_fill(0, $n + 1, $INF);
            $dist[$start] = 0;
            $pq = new SplPriorityQueue();
            $pq->insert([$start, 0], 0);
            while (!$pq->isEmpty()) {
                $cur = $pq->extract();
                $u = $cur[0];
                $d = $cur[1];
                if ($d !== $dist[$u]) continue;
                foreach ($g[$u] as $e) {
                    $v = $e[0];
                    $w = $e[1];
                    $nd = $d + $w;
                    if ($nd < $dist[$v]) {
                        $dist[$v] = $nd;
                        $pq->insert([$v, $nd], -$nd);
                    }
                }
            }
            $best = $INF;
            for ($city = 1; $city <= $n; $city++) {
                $cost = $dist[$city] * ($k + 1) + $appleCost[$city - 1];
                if ($cost < $best) $best = $cost;
            }
            $ans[$start - 1] = $best;
        }
        return $ans;
    }
}
