<?php

class Solution {
    /**
     * @param String[][] $grid
     * @return Boolean
     */
    function containsCycle($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $seen = [];

        $dfs = function ($r, $c, $pr, $pc) use (&$dfs, &$seen, $grid, $m, $n) {
            $seen["$r,$c"] = true;
            $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) {
                    continue;
                }
                if ($grid[$nr][$nc] !== $grid[$r][$c] || ($nr === $pr && $nc === $pc)) {
                    continue;
                }
                if (isset($seen["$nr,$nc"]) || $dfs($nr, $nc, $r, $c)) {
                    return true;
                }
            }
            return false;
        };

        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if (!isset($seen["$r,$c"]) && $dfs($r, $c, -1, -1)) {
                    return true;
                }
            }
        }
        return false;
    }
}
