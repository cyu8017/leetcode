<?php

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxProductPath($grid) {
        $mod = 1000000007;
        $m = count($grid);
        $n = count($grid[0]);
        $high = array_fill(0, $m, array_fill(0, $n, 0));
        $low = array_fill(0, $m, array_fill(0, $n, 0));
        $high[0][0] = $low[0][0] = $grid[0][0];

        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($r === 0 && $c === 0) {
                    continue;
                }
                $values = [];
                if ($r > 0) {
                    $values[] = $high[$r - 1][$c] * $grid[$r][$c];
                    $values[] = $low[$r - 1][$c] * $grid[$r][$c];
                }
                if ($c > 0) {
                    $values[] = $high[$r][$c - 1] * $grid[$r][$c];
                    $values[] = $low[$r][$c - 1] * $grid[$r][$c];
                }
                $high[$r][$c] = max($values);
                $low[$r][$c] = min($values);
            }
        }

        $best = $high[$m - 1][$n - 1];
        if ($best < 0) {
            return -1;
        }
        return $best % $mod;
    }
}
