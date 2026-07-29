<?php
// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

class Solution {
    /**
     * @param String $tiles
     * @return Integer
     */
    function numTilePossibilities($tiles) {
        $count = [];
        $n = strlen($tiles);
        for ($i = 0; $i < $n; $i++) {
            $ch = $tiles[$i];
            $count[$ch] = ($count[$ch] ?? 0) + 1;
        }
        $dfs = null;
        $dfs = function () use (&$dfs, &$count) {
            $total = 0;
            foreach ($count as $ch => $freq) {
                if ($freq === 0) {
                    continue;
                }
                $count[$ch]--;
                $total += 1 + $dfs();
                $count[$ch]++;
            }
            return $total;
        };
        return $dfs();
    }
}
