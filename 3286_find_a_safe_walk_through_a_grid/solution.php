<?php
// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

class Solution {
    function findSafeWalk($grid, $health) {
        $m = count($grid);
        $n = count($grid[0]);
        $vis = [];
        for ($i = 0; $i < $m; $i++) $vis[$i] = array_fill(0, $n, -1);
        $qh = $health - $grid[0][0];
        if ($qh <= 0) return false;
        $q = [[0, 0, $qh]];
        $vis[0][0] = $qh;
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $head = 0;
        while ($head < count($q)) {
            $cur = $q[$head++];
            if ($cur[0] === $m - 1 && $cur[1] === $n - 1) return true;
            foreach ($dirs as $d) {
                $nr = $cur[0] + $d[0];
                $nc = $cur[1] + $d[1];
                if ($nr < 0 || $nc < 0 || $nr >= $m || $nc >= $n) continue;
                $nh = $cur[2] - $grid[$nr][$nc];
                if ($nh <= 0) continue;
                if ($nh > $vis[$nr][$nc]) {
                    $vis[$nr][$nc] = $nh;
                    $q[] = [$nr, $nc, $nh];
                }
            }
        }
        return false;
    }
}
