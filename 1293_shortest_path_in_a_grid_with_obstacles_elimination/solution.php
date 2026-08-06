<?php
// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer
     */
    function shortestPath($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        if ($k >= $m + $n - 2) return $m + $n - 2;
        $queue = [[0, 0, $k, 0]];
        $best = ['0,0' => $k];
        $head = 0;
        while ($head < count($queue)) {
            [$r, $c, $remaining, $distance] = $queue[$head++];
            if ($r === $m - 1 && $c === $n - 1) return $distance;
            foreach ([[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                $nr = $r + $dr; $nc = $c + $dc;
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n) {
                    $nxt = $remaining - $grid[$nr][$nc];
                    $key = "$nr,$nc";
                    if ($nxt >= 0 && $nxt > ($best[$key] ?? -1)) {
                        $best[$key] = $nxt;
                        $queue[] = [$nr, $nc, $nxt, $distance + 1];
                    }
                }
            }
        }
        return -1;
    }
}
