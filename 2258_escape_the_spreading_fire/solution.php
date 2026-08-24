<?php
// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

class Solution {
    function maximumMinutes($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $inf = 1000000000;
        $fire = [];
        for ($i = 0; $i < $m; $i++) $fire[$i] = array_fill(0, $n, $inf);
        $q = [];
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] === 1) { $fire[$i][$j] = 0; $q[] = [$i, $j]; }
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $qi = 0;
        while ($qi < count($q)) {
            [$r, $c] = $q[$qi++];
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n || $grid[$nr][$nc] === 2 || $fire[$nr][$nc] !== $inf) continue;
                $fire[$nr][$nc] = $fire[$r][$c] + 1;
                $q[] = [$nr, $nc];
            }
        }
        $can = function($wait) use ($m, $n, $grid, $fire, $dirs) {
            if ($wait >= $fire[0][0]) return false;
            $vis = [];
            for ($i = 0; $i < $m; $i++) $vis[$i] = array_fill(0, $n, false);
            $qq = [[0, 0, $wait]];
            $vis[0][0] = true;
            $qi = 0;
            while ($qi < count($qq)) {
                [$r, $c, $t] = $qq[$qi++];
                foreach ($dirs as $d) {
                    $nr = $r + $d[0];
                    $nc = $c + $d[1];
                    $nt = $t + 1;
                    if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n || $grid[$nr][$nc] === 2 || $vis[$nr][$nc]) continue;
                    if ($nr === $m - 1 && $nc === $n - 1) {
                        if ($nt <= $fire[$nr][$nc]) return true;
                        continue;
                    }
                    if ($nt >= $fire[$nr][$nc]) continue;
                    $vis[$nr][$nc] = true;
                    $qq[] = [$nr, $nc, $nt];
                }
            }
            return false;
        };
        $lo = 0;
        $hi = $m * $n + 10;
        $ans = -1;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($can($mid)) { $ans = $mid; $lo = $mid + 1; }
            else $hi = $mid - 1;
        }
        if ($ans >= $m * $n) return $inf;
        return $ans;
    }
}
