<?php
// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution {
    function knightProbability($n, $k, $row, $column) {
        $moves = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]];
        $dp = array_fill(0, $n, array_fill(0, $n, 0.0));
        $dp[$row][$column] = 1.0;
        for ($step = 0; $step < $k; $step++) {
            $nxt = array_fill(0, $n, array_fill(0, $n, 0.0));
            for ($r = 0; $r < $n; $r++) {
                for ($c = 0; $c < $n; $c++) {
                    if ($dp[$r][$c] === 0.0) continue;
                    foreach ($moves as $move) {
                        $nr = $r + $move[0];
                        $nc = $c + $move[1];
                        if ($nr >= 0 && $nr < $n && $nc >= 0 && $nc < $n) $nxt[$nr][$nc] += $dp[$r][$c] / 8.0;
                    }
                }
            }
            $dp = $nxt;
        }
        $total = 0.0;
        for ($r = 0; $r < $n; $r++)
            for ($c = 0; $c < $n; $c++)
                $total += $dp[$r][$c];
        return $total;
    }
}
