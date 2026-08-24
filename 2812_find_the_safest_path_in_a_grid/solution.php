<?php
// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

class Solution {
    function maximumSafenessFactor($grid) {
        $n = count($grid);
        $dist = array_fill(0, $n, array_fill(0, $n, -1));
        $q = [];
        for ($i = 0; $i < $n; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] === 1) {
                    $dist[$i][$j] = 0;
                    $q[] = [$i, $j];
                }
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        for ($h = 0; $h < count($q); $h++) {
            $x = $q[$h][0];
            $y = $q[$h][1];
            foreach ($dirs as $d) {
                $ni = $x + $d[0];
                $nj = $y + $d[1];
                if ($ni >= 0 && $nj >= 0 && $ni < $n && $nj < $n && $dist[$ni][$nj] === -1) {
                    $dist[$ni][$nj] = $dist[$x][$y] + 1;
                    $q[] = [$ni, $nj];
                }
            }
        }
        $ok = function($sf) use ($n, $dist, $dirs) {
            if ($dist[0][0] < $sf) return false;
            $seen = array_fill(0, $n, array_fill(0, $n, false));
            $st = [[0, 0]];
            $seen[0][0] = true;
            while ($st) {
                $cur = array_pop($st);
                $x = $cur[0];
                $y = $cur[1];
                if ($x === $n - 1 && $y === $n - 1) return true;
                foreach ($dirs as $d) {
                    $ni = $x + $d[0];
                    $nj = $y + $d[1];
                    if ($ni >= 0 && $nj >= 0 && $ni < $n && $nj < $n && !$seen[$ni][$nj] && $dist[$ni][$nj] >= $sf) {
                        $seen[$ni][$nj] = true;
                        $st[] = [$ni, $nj];
                    }
                }
            }
            return false;
        };
        $lo = 0;
        $hi = $n * $n;
        $ans = 0;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($ok($mid)) { $ans = $mid; $lo = $mid + 1; }
            else $hi = $mid - 1;
        }
        return $ans;
    }
}
