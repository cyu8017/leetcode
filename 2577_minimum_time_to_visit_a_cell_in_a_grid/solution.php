<?php
// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

class Solution {
    function minimumTime($grid) {
        if ($grid[0][1] > 1 && $grid[1][0] > 1) return -1;
        $m = count($grid);
        $n = count($grid[0]);
        $INF = 1 << 30;
        $dist = [];
        for ($i = 0; $i < $m; $i++) $dist[] = array_fill(0, $n, $INF);
        $h = new SplPriorityQueue();
        $h->insert([0, 0, 0], 0);
        $dist[0][0] = 0;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (!$h->isEmpty()) {
            $cur = $h->extract();
            $t = $cur[0];
            $r = $cur[1];
            $c = $cur[2];
            if ($r === $m - 1 && $c === $n - 1) return $t;
            if ($t > $dist[$r][$c]) continue;
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                $nt = $t + 1;
                if ($nt < $grid[$nr][$nc]) {
                    $wait = $grid[$nr][$nc] - $nt;
                    if ($wait % 2 === 1) $wait++;
                    $nt += $wait;
                }
                if ($nt < $dist[$nr][$nc]) {
                    $dist[$nr][$nc] = $nt;
                    $h->insert([$nt, $nr, $nc], -$nt);
                }
            }
        }
        return -1;
    }
}
