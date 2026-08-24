<?php
// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

class Solution {
    function minTimeMaxPower($n, $edges, $power, $cost, $source, $target) {
        $INF = PHP_INT_MAX / 4;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) $g[$e[0]][] = [$e[1], $e[2]];
        $dist = array_fill(0, $n, array_fill(0, $power + 1, $INF));
        $dist[$source][$power] = 0;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0, $power, $source], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $d = $cur[0];
            $p = $cur[1];
            $u = $cur[2];
            if ($u === $target) return [$d, $p];
            if ($d > $dist[$u][$p] || $p < $cost[$u]) continue;
            $p -= $cost[$u];
            foreach ($g[$u] as $e) {
                $v = $e[0];
                $t = $e[1];
                $nd = $d + $t;
                if ($nd < $dist[$v][$p]) {
                    $dist[$v][$p] = $nd;
                    $pq->insert([$nd, $p, $v], -$nd);
                }
            }
        }
        return [-1, -1];
    }
}
