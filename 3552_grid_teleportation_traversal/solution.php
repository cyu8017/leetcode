<?php
// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

class Solution {
    function minMoves($matrix) {
        $m = count($matrix);
        $n = strlen($matrix[0]);
        $g = [];
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++) {
                $c = $matrix[$i][$j];
                if (($c >= 'A' && $c <= 'Z') || ($c >= 'a' && $c <= 'z')) {
                    if (!isset($g[$c])) $g[$c] = [];
                    $g[$c][] = [$i, $j];
                }
            }
        $dirs = [-1, 0, 1, 0, -1];
        $INF = 1 << 30;
        $dist = [];
        for ($i = 0; $i < $m; $i++) $dist[$i] = array_fill(0, $n, $INF);
        $dist[0][0] = 0;
        $q = [[0, 0]];
        while (count($q)) {
            $cur = array_shift($q);
            $i = $cur[0];
            $j = $cur[1];
            $d = $dist[$i][$j];
            if ($i === $m - 1 && $j === $n - 1) return $d;
            $c = $matrix[$i][$j];
            if (isset($g[$c])) {
                foreach ($g[$c] as $p) {
                    $x = $p[0];
                    $y = $p[1];
                    if ($d < $dist[$x][$y]) {
                        $dist[$x][$y] = $d;
                        array_unshift($q, [$x, $y]);
                    }
                }
                unset($g[$c]);
            }
            for ($idx = 0; $idx < 4; $idx++) {
                $x = $i + $dirs[$idx];
                $y = $j + $dirs[$idx + 1];
                if (0 <= $x && $x < $m && 0 <= $y && $y < $n && $matrix[$x][$y] !== '#' && $d + 1 < $dist[$x][$y]) {
                    $dist[$x][$y] = $d + 1;
                    $q[] = [$x, $y];
                }
            }
        }
        return -1;
    }
}
