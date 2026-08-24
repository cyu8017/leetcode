<?php
// LeetCode 3797 - Count Routes to Climb a Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

class Solution {
    function countRoutes($grid, $d) {
        $MOD = 1000000007;
        $n = count($grid);
        $m = count($grid[0]);
        $upRadius = 0;
        while (($upRadius + 1) * ($upRadius + 1) + 1 <= $d * $d) $upRadius++;
        $arrived = array_fill(0, $m, 0);
        for ($c = 0; $c < $m; $c++) {
            if ($grid[$n - 1][$c] === '.') $arrived[$c] = 1;
        }
        for ($r = $n - 1; $r >= 0; $r--) {
            $pref = array_fill(0, $m + 1, 0);
            for ($i = 0; $i < $m; $i++) $pref[$i + 1] = ($pref[$i] + $arrived[$i]) % $MOD;
            $horizontal = array_fill(0, $m, 0);
            for ($c = 0; $c < $m; $c++) {
                if ($grid[$r][$c] === '#') continue;
                $l = max(0, $c - $d);
                $rr = min($m - 1, $c + $d);
                $horizontal[$c] = ($pref[$rr + 1] - $pref[$l] - $arrived[$c]) % $MOD;
                if ($horizontal[$c] < 0) $horizontal[$c] += $MOD;
            }
            if ($r === 0) {
                $ans = 0;
                for ($c = 0; $c < $m; $c++) $ans = ($ans + $arrived[$c] + $horizontal[$c]) % $MOD;
                return $ans;
            }
            $pref2 = array_fill(0, $m + 1, 0);
            for ($c = 0; $c < $m; $c++) $pref2[$c + 1] = ($pref2[$c] + $arrived[$c] + $horizontal[$c]) % $MOD;
            $next = array_fill(0, $m, 0);
            for ($c = 0; $c < $m; $c++) {
                if ($grid[$r - 1][$c] === '#') continue;
                $l = max(0, $c - $upRadius);
                $rr = min($m - 1, $c + $upRadius);
                $next[$c] = $pref2[$rr + 1] - $pref2[$l];
                if ($next[$c] < 0) $next[$c] += $MOD;
            }
            $arrived = $next;
        }
        return 0;
    }
}
