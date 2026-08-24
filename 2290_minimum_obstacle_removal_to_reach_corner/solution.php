<?php
// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution {
    function minimumObstacles($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $INF = PHP_INT_MAX / 4;
        $dist = [];
        for ($i = 0; $i < $m; $i++) $dist[$i] = array_fill(0, $n, $INF);
        $dist[0][0] = 0;
        $dq = [[0, 0]];
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (count($dq)) {
            [$r, $c] = array_shift($dq);
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                $nd = $dist[$r][$c] + $grid[$nr][$nc];
                if ($nd < $dist[$nr][$nc]) {
                    $dist[$nr][$nc] = $nd;
                    if ($grid[$nr][$nc] === 0) array_unshift($dq, [$nr, $nc]);
                    else $dq[] = [$nr, $nc];
                }
            }
        }
        return $dist[$m - 1][$n - 1];
    }
}
