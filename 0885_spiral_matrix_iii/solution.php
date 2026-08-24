<?php
// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

class Solution {
    function spiralMatrixIII($rows, $cols, $rStart, $cStart) {
        $ans = [[$rStart, $cStart]];
        if ($rows * $cols === 1) return $ans;
        $r = $rStart;
        $c = $cStart;
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        $steps = 1;
        while (count($ans) < $rows * $cols) {
            for ($d = 0; $d < 4; $d++) {
                [$dr, $dc] = $dirs[$d];
                for ($i = 0; $i < $steps; $i++) {
                    $r += $dr;
                    $c += $dc;
                    if ($r >= 0 && $r < $rows && $c >= 0 && $c < $cols) {
                        $ans[] = [$r, $c];
                        if (count($ans) === $rows * $cols) return $ans;
                    }
                }
                if ($d % 2 === 1) $steps++;
            }
        }
        return $ans;
    }
}
