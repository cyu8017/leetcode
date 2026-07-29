<?php
// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function shortestPathBinaryMatrix($grid) {
        $n = count($grid);
        if ($grid[0][0] || $grid[$n - 1][$n - 1]) {
            return -1;
        }
        $queue = [[0, 0, 1]];
        $grid[0][0] = 1;
        $head = 0;
        while ($head < count($queue)) {
            [$r, $c, $dist] = $queue[$head++];
            if ($r === $n - 1 && $c === $n - 1) {
                return $dist;
            }
            for ($dr = -1; $dr <= 1; $dr++) {
                for ($dc = -1; $dc <= 1; $dc++) {
                    if ($dr === 0 && $dc === 0) {
                        continue;
                    }
                    $nr = $r + $dr;
                    $nc = $c + $dc;
                    if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n && $grid[$nr][$nc] === 0) {
                        $grid[$nr][$nc] = 1;
                        $queue[] = [$nr, $nc, $dist + 1];
                    }
                }
            }
        }
        return -1;
    }
}
