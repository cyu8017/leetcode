<?php
// LeetCode 4003 - Minimum Cost Path with Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

class Solution {
    function minCost($m, $n, $penalty) {
        $INF = 1 << 60;
        $dist = array_fill(0, $m, array_fill(0, $n, [$INF, $INF]));
        $dist[0][0][1] = 1;
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([1, 0, 0, 1], -1);
        $dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]];
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $d = $cur[0];
            $i = $cur[1];
            $j = $cur[2];
            $k = $cur[3];
            if ($i === $m - 1 && $j === $n - 1) return $d;
            if ($d > $dist[$i][$j][$k]) continue;
            $p = $penalty[$i][$j];
            $nd = $d + $p;
            if ($nd < $dist[$i][$j][$k ^ 1]) {
                $dist[$i][$j][$k ^ 1] = $nd;
                $pq->insert([$nd, $i, $j, $k ^ 1], -$nd);
            }
            for ($idx = 0; $idx < 4; $idx++) {
                $x = $i + $dirs[$idx][0];
                $y = $j + $dirs[$idx][1];
                if (0 <= $x && $x < $m && 0 <= $y && $y < $n) {
                    $nd = $d + (($x + 1) * ($y + 1) + ((($idx & 1) ^ $k) * $p));
                    if ($nd < $dist[$x][$y][$k ^ 1]) {
                        $dist[$x][$y][$k ^ 1] = $nd;
                        $pq->insert([$nd, $x, $y, $k ^ 1], -$nd);
                    }
                }
            }
        }
        return -1;
    }
}
