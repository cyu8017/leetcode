<?php
// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

class Solution {
    private $memo = [];

    /**
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function minKnightMoves($x, $y) {
        return $this->dfs(abs($x), abs($y));
    }

    private function dfs($a, $b) {
        if ($a + $b === 0) return 0;
        if ($a + $b === 2) return 2;
        $key = "$a,$b";
        if (isset($this->memo[$key])) return $this->memo[$key];
        return $this->memo[$key] = min(
            $this->dfs(abs($a - 1), abs($b - 2)),
            $this->dfs(abs($a - 2), abs($b - 1))
        ) + 1;
    }
}
