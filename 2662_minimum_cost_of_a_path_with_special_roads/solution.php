<?php
// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

class Solution {
    function minimumCost($start, $target, $specialRoads) {
        $points = [$start, $target];
        foreach ($specialRoads as $r) {
            $points[] = [$r[0], $r[1]];
            $points[] = [$r[2], $r[3]];
        }
        $N = count($points);
        $man = function($a, $b) {
            return abs($a[0] - $b[0]) + abs($a[1] - $b[1]);
        };
        $g = array_fill(0, $N, []);
        for ($i = 0; $i < $N; $i++) {
            for ($j = 0; $j < $N; $j++) {
                if ($i !== $j) $g[$i][] = [$j, $man($points[$i], $points[$j])];
            }
        }
        foreach ($specialRoads as $r) {
            $u = -1;
            $v = -1;
            for ($i = 0; $i < $N; $i++) {
                $p = $points[$i];
                if ($p[0] === $r[0] && $p[1] === $r[1]) $u = $i;
                if ($p[0] === $r[2] && $p[1] === $r[3]) $v = $i;
            }
            if ($u >= 0 && $v >= 0) $g[$u][] = [$v, $r[4]];
        }
        $INF = PHP_INT_MAX >> 2;
        $dist = array_fill(0, $N, $INF);
        $dist[0] = 0;
        $pq = new SplPriorityQueue();
        $pq->insert([0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $id = $cur[0];
            $cost = $cur[1];
            if ($cost > $dist[$id]) continue;
            foreach ($g[$id] as $e) {
                $to = $e[0];
                $w = $e[1];
                if ($cost + $w < $dist[$to]) {
                    $dist[$to] = $cost + $w;
                    $pq->insert([$to, $dist[$to]], -$dist[$to]);
                }
            }
        }
        return $dist[1];
    }
}
