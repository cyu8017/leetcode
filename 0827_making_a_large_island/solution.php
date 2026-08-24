<?php
// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largestIsland($grid) {
        $n = count($grid);
        $sizes = [0 => 0];
        $islandId = 2;
        $dfs = function($r, $c, $iid) use (&$dfs, &$grid, $n) {
            if ($r < 0 || $r >= $n || $c < 0 || $c >= $n || $grid[$r][$c] !== 1) return 0;
            $grid[$r][$c] = $iid;
            return 1 + $dfs($r + 1, $c, $iid) + $dfs($r - 1, $c, $iid) + $dfs($r, $c + 1, $iid) + $dfs($r, $c - 1, $iid);
        };
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 1) {
                    $sizes[$islandId] = $dfs($i, $j, $islandId);
                    $islandId++;
                }
            }
        }
        $ans = 0;
        foreach ($sizes as $v) $ans = max($ans, $v);
        $dr = [1, -1, 0, 0];
        $dc = [0, 0, 1, -1];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] !== 0) continue;
                $seen = [];
                $total = 1;
                for ($k = 0; $k < 4; $k++) {
                    $ni = $i + $dr[$k];
                    $nj = $j + $dc[$k];
                    if ($ni >= 0 && $ni < $n && $nj >= 0 && $nj < $n) {
                        $iid = $grid[$ni][$nj];
                        if ($iid > 1 && !isset($seen[$iid])) {
                            $seen[$iid] = true;
                            $total += $sizes[$iid];
                        }
                    }
                }
                $ans = max($ans, $total);
            }
        }
        return $ans;
    }
}
