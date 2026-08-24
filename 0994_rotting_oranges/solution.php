<?php
// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function orangesRotting($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $q = [];
        $fresh = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 2) $q[] = [$i, $j];
                else if ($grid[$i][$j] === 1) $fresh++;
            }
        }
        $minutes = 0;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while ($q && $fresh > 0) {
            $sz = count($q);
            for ($s = 0; $s < $sz; $s++) {
                [$cr, $cc] = array_shift($q);
                foreach ($dirs as $d) {
                    $nr = $cr + $d[0];
                    $nc = $cc + $d[1];
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $grid[$nr][$nc] === 1) {
                        $grid[$nr][$nc] = 2;
                        $fresh--;
                        $q[] = [$nr, $nc];
                    }
                }
            }
            $minutes++;
        }
        return $fresh === 0 ? $minutes : -1;
    }
}
