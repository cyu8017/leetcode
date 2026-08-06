<?php
// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

class Solution {
    function countSubIslands($grid1, $grid2) {
        $rows = count($grid2);
        $cols = count($grid2[0]);
        $ans = 0;
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                if ($grid2[$r][$c] === 1 && $this->dfs($grid1, $grid2, $r, $c, $rows, $cols)) {
                    $ans++;
                }
            }
        }
        return $ans;
    }

    private function dfs(&$grid1, &$grid2, $r, $c, $rows, $cols) {
        if ($r < 0 || $c < 0 || $r >= $rows || $c >= $cols || $grid2[$r][$c] === 0) {
            return true;
        }
        $grid2[$r][$c] = 0;
        $ok = $grid1[$r][$c] === 1;
        foreach ([[$r + 1, $c], [$r - 1, $c], [$r, $c + 1], [$r, $c - 1]] as $next) {
            if (!$this->dfs($grid1, $grid2, $next[0], $next[1], $rows, $cols)) {
                $ok = false;
            }
        }
        return $ok;
    }
}
