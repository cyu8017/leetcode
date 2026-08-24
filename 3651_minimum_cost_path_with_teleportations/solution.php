<?php
// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

class Solution {
    function minCost($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $inf = 536870911;
        $f = [];
        for ($t = 0; $t <= $k; $t++) {
            $f[$t] = [];
            for ($i = 0; $i < $m; $i++) $f[$t][$i] = array_fill(0, $n, $inf);
        }
        $f[0][0][0] = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i > 0) $f[0][$i][$j] = min($f[0][$i][$j], $f[0][$i - 1][$j] + $grid[$i][$j]);
                if ($j > 0) $f[0][$i][$j] = min($f[0][$i][$j], $f[0][$i][$j - 1] + $grid[$i][$j]);
            }
        }
        $g = [];
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++) {
                if (!isset($g[$grid[$i][$j]])) $g[$grid[$i][$j]] = [];
                $g[$grid[$i][$j]][] = [$i, $j];
            }
        $keys = array_keys($g);
        rsort($keys);
        for ($t = 1; $t <= $k; $t++) {
            $mn = $inf;
            foreach ($keys as $key) {
                $pos = $g[$key];
                foreach ($pos as $p) $mn = min($mn, $f[$t - 1][$p[0]][$p[1]]);
                foreach ($pos as $p) $f[$t][$p[0]][$p[1]] = $mn;
            }
            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    if ($i > 0) $f[$t][$i][$j] = min($f[$t][$i][$j], $f[$t][$i - 1][$j] + $grid[$i][$j]);
                    if ($j > 0) $f[$t][$i][$j] = min($f[$t][$i][$j], $f[$t][$i][$j - 1] + $grid[$i][$j]);
                }
            }
        }
        $ans = $inf;
        for ($t = 0; $t <= $k; $t++) $ans = min($ans, $f[$t][$m - 1][$n - 1]);
        return $ans;
    }
}
