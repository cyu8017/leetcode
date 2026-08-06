<?php
// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function closedIsland($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $flood = function ($sr, $sc) use (&$grid, $m, $n) {
            $stack = [[$sr, $sc]];
            $closed = true;
            $grid[$sr][$sc] = 1;
            while (!empty($stack)) {
                [$r, $c] = array_pop($stack);
                if ($r === 0 || $r === $m - 1 || $c === 0 || $c === $n - 1) $closed = false;
                foreach ([[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                    $nr = $r + $dr; $nc = $c + $dc;
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $grid[$nr][$nc] === 0) {
                        $grid[$nr][$nc] = 1;
                        $stack[] = [$nr, $nc];
                    }
                }
            }
            return $closed;
        };
        $ans = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c] === 0 && $flood($r, $c)) $ans++;
            }
        }
        return $ans;
    }
}
