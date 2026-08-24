<?php
// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

class Solution {
    function checkValidGrid($grid) {
        $n = count($grid);
        if ($grid[0][0] !== 0) return false;
        $pos = array_fill(0, $n * $n, null);
        for ($i = 0; $i < $n; $i++)
            for ($j = 0; $j < $n; $j++)
                $pos[$grid[$i][$j]] = [$i, $j];
        $dirs = [
            [1, 2], [1, -2], [-1, 2], [-1, -2],
            [2, 1], [2, -1], [-2, 1], [-2, -1],
        ];
        for ($v = 0; $v + 1 < $n * $n; $v++) {
            $r = $pos[$v][0];
            $c = $pos[$v][1];
            $ok = false;
            foreach ($dirs as $d) {
                if ($r + $d[0] === $pos[$v + 1][0] && $c + $d[1] === $pos[$v + 1][1]) {
                    $ok = true;
                    break;
                }
            }
            if (!$ok) return false;
        }
        return true;
    }
}
