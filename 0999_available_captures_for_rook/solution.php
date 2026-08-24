<?php
// LeetCode 0999 - Available Captures for Rook
// https://leetcode.com/problems/available-captures-for-rook/

class Solution {
    /**
     * @param String[][] $board
     * @return Integer
     */
    function numRookCaptures($board) {
        $m = count($board);
        $n = count($board[0]);
        $r = -1;
        $c = -1;
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($board[$i][$j] === 'R') { $r = $i; $c = $j; }
        if ($r < 0) return 0;
        $ans = 0;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        foreach ($dirs as $d) {
            $i = $r + $d[0];
            $j = $c + $d[1];
            while ($i >= 0 && $i < $m && $j >= 0 && $j < $n) {
                if ($board[$i][$j] === 'B') break;
                if ($board[$i][$j] === 'p') { $ans++; break; }
                $i += $d[0];
                $j += $d[1];
            }
        }
        return $ans;
    }
}
