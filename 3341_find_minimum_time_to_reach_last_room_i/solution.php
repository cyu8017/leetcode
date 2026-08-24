<?php
// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

class Solution {
    function minTimeToReach($moveTime) {
        $m = count($moveTime);
        $n = count($moveTime[0]);
        $dist = [];
        for ($i = 0; $i < $m; $i++) $dist[$i] = array_fill(0, $n, 1 << 30);
        $h = [[0, 0, 0]];
        $dist[0][0] = 0;
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([0, 0, 0], 0);
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $t = $cur[0];
            $r = $cur[1];
            $c = $cur[2];
            if ($t !== $dist[$r][$c]) continue;
            if ($r === $m - 1 && $c === $n - 1) return $t;
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nc < 0 || $nr >= $m || $nc >= $n) continue;
                $start = max($t, $moveTime[$nr][$nc]);
                $nt = $start + 1;
                if ($nt < $dist[$nr][$nc]) {
                    $dist[$nr][$nc] = $nt;
                    $pq->insert([$nt, $nr, $nc], -$nt);
                }
            }
        }
        return -1;
    }
}
