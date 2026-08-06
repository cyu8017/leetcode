<?php
// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumMoves($grid) {
        $n = count($grid);
        $start = '0,0,0';
        $target = ($n - 1) . ',' . ($n - 2) . ',0';
        $queue = [[0, 0, 0, 0]];
        $seen = [$start => true];
        $head = 0;
        while ($head < count($queue)) {
            [$r, $c, $orient, $moves] = $queue[$head++];
            if ("$r,$c,$orient" === $target) return $moves;
            $nxt = [];
            if ($orient === 0) {
                if ($c + 2 < $n && $grid[$r][$c + 2] === 0) $nxt[] = [$r, $c + 1, 0];
                if ($r + 1 < $n && $grid[$r + 1][$c] === 0 && $grid[$r + 1][$c + 1] === 0) {
                    $nxt[] = [$r + 1, $c, 0];
                    $nxt[] = [$r, $c, 1];
                }
            } else {
                if ($r + 2 < $n && $grid[$r + 2][$c] === 0) $nxt[] = [$r + 1, $c, 1];
                if ($c + 1 < $n && $grid[$r][$c + 1] === 0 && $grid[$r + 1][$c + 1] === 0) {
                    $nxt[] = [$r, $c + 1, 1];
                    $nxt[] = [$r, $c, 0];
                }
            }
            foreach ($nxt as [$nr, $nc, $no]) {
                $key = "$nr,$nc,$no";
                if (!isset($seen[$key])) {
                    $seen[$key] = true;
                    $queue[] = [$nr, $nc, $no, $moves + 1];
                }
            }
        }
        return -1;
    }
}
