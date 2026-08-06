<?php
// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxDistance($grid) {
        $n = count($grid);
        $queue = [];
        for ($r = 0; $r < $n; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c] === 1) $queue[] = [$r, $c];
            }
        }
        if (empty($queue) || count($queue) === $n * $n) return -1;
        $dist = -1;
        $head = 0;
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        while ($head < count($queue)) {
            $dist++;
            $sz = count($queue) - $head;
            for ($i = 0; $i < $sz; $i++) {
                [$r, $c] = $queue[$head++];
                foreach ($dirs as [$dr, $dc]) {
                    $nr = $r + $dr; $nc = $c + $dc;
                    if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n && $grid[$nr][$nc] === 0) {
                        $grid[$nr][$nc] = 1;
                        $queue[] = [$nr, $nc];
                    }
                }
            }
        }
        return $dist;
    }
}
