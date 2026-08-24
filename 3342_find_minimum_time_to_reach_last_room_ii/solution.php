<?php
// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

class Solution {
    function minTimeToReach($moveTime) {
        $m = count($moveTime);
        $n = count($moveTime[0]);
        $INF = 1 << 30;
        $dist = [];
        for ($i = 0; $i < $m; $i++) {
            $dist[$i] = [];
            for ($j = 0; $j < $n; $j++) $dist[$i][$j] = [$INF, $INF];
        }
        $dist[0][0][0] = 0;
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0, 0, 0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $t = $cur[0];
            $r = $cur[1];
            $c = $cur[2];
            $parity = $cur[3];
            if ($t !== $dist[$r][$c][$parity]) continue;
            if ($r === $m - 1 && $c === $n - 1) return $t;
            $cost = $parity === 1 ? 2 : 1;
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nc < 0 || $nr >= $m || $nc >= $n) continue;
                $start = max($t, $moveTime[$nr][$nc]);
                $nt = $start + $cost;
                $np = 1 - $parity;
                if ($nt < $dist[$nr][$nc][$np]) {
                    $dist[$nr][$nc][$np] = $nt;
                    $pq->insert([$nt, $nr, $nc, $np], -$nt);
                }
            }
        }
        return -1;
    }
}
