<?php
class Solution {
    function minCost($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dist = array_fill(0, $m, array_fill(0, $n, 1000000000));
        $dist[0][0] = 0;
        $q = [[0, 0]];
        $dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        while ($q) {
            [$r, $c] = array_shift($q);
            foreach ($dirs as $k => [$dr, $dc]) {
                $x = $r + $dr;
                $y = $c + $dc;
                if ($x >= 0 && $x < $m && $y >= 0 && $y < $n) {
                    $w = ($k + 1) !== $grid[$r][$c] ? 1 : 0;
                    $nd = $dist[$r][$c] + $w;
                    if ($nd < $dist[$x][$y]) {
                        $dist[$x][$y] = $nd;
                        if ($w) $q[] = [$x, $y];
                        else array_unshift($q, [$x, $y]);
                    }
                }
            }
        }
        return $dist[$m - 1][$n - 1];
    }
}
