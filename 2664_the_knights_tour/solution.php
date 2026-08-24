<?php
// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

class Solution {
    function tourOfKnight($m, $n, $r, $c) {
        $DIRS = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]];
        $ans = [];
        for ($i = 0; $i < $m; $i++) $ans[$i] = array_fill(0, $n, -1);
        $dfs = function($x, $y, $step) use (&$dfs, &$ans, $DIRS, $m, $n) {
            $ans[$x][$y] = $step;
            if ($step === $m * $n - 1) return true;
            foreach ($DIRS as $d) {
                $nx = $x + $d[0];
                $ny = $y + $d[1];
                if ($nx >= 0 && $nx < $m && $ny >= 0 && $ny < $n && $ans[$nx][$ny] === -1) {
                    if ($dfs($nx, $ny, $step + 1)) return true;
                }
            }
            $ans[$x][$y] = -1;
            return false;
        };
        $dfs($r, $c, 0);
        return $ans;
    }
}
