<?php

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minDays($grid) {
        $m = count($grid);
        $n = count($grid[0]);

        $islands = function () use (&$grid, $m, $n) {
            $seen = [];
            $count = 0;
            for ($r = 0; $r < $m; $r++) {
                for ($c = 0; $c < $n; $c++) {
                    if ($grid[$r][$c] && !isset($seen["$r,$c"])) {
                        $count++;
                        $stack = [[$r, $c]];
                        $seen["$r,$c"] = true;
                        while ($stack) {
                            [$x, $y] = array_pop($stack);
                            foreach ([[1, 0], [-1, 0], [0, 1], [0, -1]] as $d) {
                                $nx = $x + $d[0];
                                $ny = $y + $d[1];
                                if ($nx >= 0 && $nx < $m && $ny >= 0 && $ny < $n
                                    && $grid[$nx][$ny] && !isset($seen["$nx,$ny"])) {
                                    $seen["$nx,$ny"] = true;
                                    $stack[] = [$nx, $ny];
                                }
                            }
                        }
                    }
                }
            }
            return $count;
        };

        if ($islands() !== 1) {
            return 0;
        }
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c]) {
                    $grid[$r][$c] = 0;
                    if ($islands() !== 1) {
                        $grid[$r][$c] = 1;
                        return 1;
                    }
                    $grid[$r][$c] = 1;
                }
            }
        }
        return 2;
    }
}
