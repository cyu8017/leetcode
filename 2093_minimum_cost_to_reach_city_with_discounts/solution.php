<?php
// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $highways
     * @param Integer $discounts
     * @return Integer
     */
    function minimumCost($n, $highways, $discounts) {
        $g = array_fill(0, $n, []);
        foreach ($highways as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $INF = 1 << 30;
        $dist = [];
        for ($i = 0; $i < $n; $i++) $dist[$i] = array_fill(0, $discounts + 1, $INF);
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $dist[0][$discounts] = 0;
        $pq->insert([0, 0, $discounts], 0);
        while (!$pq->isEmpty()) {
            [$cost, $city, $disc] = $pq->extract();
            if ($city === $n - 1) return $cost;
            if ($cost > $dist[$city][$disc]) continue;
            foreach ($g[$city] as $e) {
                $v = $e[0];
                $w = $e[1];
                if ($cost + $w < $dist[$v][$disc]) {
                    $dist[$v][$disc] = $cost + $w;
                    $pq->insert([$dist[$v][$disc], $v, $disc], -$dist[$v][$disc]);
                }
                if ($disc > 0 && $cost + intdiv($w, 2) < $dist[$v][$disc - 1]) {
                    $dist[$v][$disc - 1] = $cost + intdiv($w, 2);
                    $pq->insert([$dist[$v][$disc - 1], $v, $disc - 1], -$dist[$v][$disc - 1]);
                }
            }
        }
        return -1;
    }
}
