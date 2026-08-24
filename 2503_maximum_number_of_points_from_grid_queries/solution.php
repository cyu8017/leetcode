<?php
// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

class Solution {
    function maxPoints($grid, $queries) {
        $m = count($grid);
        $n = count($grid[0]);
        $order = range(0, count($queries) - 1);
        usort($order, function ($a, $b) use ($queries) {
            return $queries[$a] <=> $queries[$b];
        });
        $ans = array_fill(0, count($queries), 0);
        $visited = [];
        for ($i = 0; $i < $m; $i++) $visited[] = array_fill(0, $n, false);
        $visited[0][0] = true;
        $points = 0;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $heap = new SplPriorityQueue();
        $heap->insert([$grid[0][0], 0, 0], -$grid[0][0]);
        foreach ($order as $qi) {
            $q = $queries[$qi];
            while (!$heap->isEmpty()) {
                $top = $heap->top();
                if ($top[0] >= $q) break;
                $cur = $heap->extract();
                $r = $cur[1];
                $c = $cur[2];
                $points++;
                foreach ($dirs as $d) {
                    $nr = $r + $d[0];
                    $nc = $c + $d[1];
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && !$visited[$nr][$nc]) {
                        $visited[$nr][$nc] = true;
                        $heap->insert([$grid[$nr][$nc], $nr, $nc], -$grid[$nr][$nc]);
                    }
                }
            }
            $ans[$qi] = $points;
        }
        return $ans;
    }
}
