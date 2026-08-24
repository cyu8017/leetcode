<?php
// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

class Solution {
    function numDistinctIslands2($grid) {
        if ($grid === null || count($grid) === 0) return 0;
        $m = count($grid);
        $n = count($grid[0]);
        $dfs = function ($r, $c, &$cells) use (&$dfs, &$grid, $m, $n) {
            if ($r < 0 || $r >= $m || $c < 0 || $c >= $n || $grid[$r][$c] === 0) return;
            $grid[$r][$c] = 0;
            $cells[] = [$r, $c];
            $dfs($r + 1, $c, $cells);
            $dfs($r - 1, $c, $cells);
            $dfs($r, $c + 1, $cells);
            $dfs($r, $c - 1, $cells);
        };
        $canonical = function ($cells) {
            $signs = [
                [1, 1, 0], [1, -1, 0], [-1, 1, 0], [-1, -1, 0],
                [1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1]
            ];
            $best = null;
            foreach ($signs as $s) {
                $pts = [];
                foreach ($cells as $p) {
                    $x = $p[0];
                    $y = $p[1];
                    if ($s[2] === 0) { $nx = $s[0] * $x; $ny = $s[1] * $y; }
                    else { $nx = $s[0] * $y; $ny = $s[1] * $x; }
                    $pts[] = [$nx, $ny];
                }
                $minX = PHP_INT_MAX;
                $minY = PHP_INT_MAX;
                foreach ($pts as $p) {
                    $minX = min($minX, $p[0]);
                    $minY = min($minY, $p[1]);
                }
                for ($i = 0; $i < count($pts); $i++) {
                    $pts[$i][0] -= $minX;
                    $pts[$i][1] -= $minY;
                }
                usort($pts, function ($a, $b) {
                    return $a[0] !== $b[0] ? $a[0] - $b[0] : $a[1] - $b[1];
                });
                $parts = [];
                foreach ($pts as $p) $parts[] = $p[0] . ',' . $p[1];
                $key = implode(';', $parts);
                if ($best === null || $key < $best) $best = $key;
            }
            return $best;
        };
        $shapes = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 1) {
                    $cells = [];
                    $dfs($i, $j, $cells);
                    $shapes[$canonical($cells)] = true;
                }
            }
        }
        return count($shapes);
    }
}
