<?php
// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

class Solution {
    function minimumSeconds($land) {
        $m = count($land);
        $n = count($land[0]);
        $INF = 1000000000;
        $water = array_fill(0, $m, array_fill(0, $n, $INF));
        $wq = [];
        $sx = 0;
        $sy = 0;
        $dx = 0;
        $dy = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $cell = $land[$i][$j];
                if ($cell === '*') {
                    $water[$i][$j] = 0;
                    $wq[] = [$i, $j];
                } else if ($cell === 'S') { $sx = $i; $sy = $j; }
                else if ($cell === 'D') { $dx = $i; $dy = $j; }
            }
        }
        $dirs = [[1,0],[-1,0],[0,1],[0,-1]];
        for ($h = 0; $h < count($wq); $h++) {
            $x = $wq[$h][0];
            $y = $wq[$h][1];
            foreach ($dirs as $d) {
                $ni = $x + $d[0];
                $nj = $y + $d[1];
                if ($ni < 0 || $nj < 0 || $ni >= $m || $nj >= $n) continue;
                $cell = $land[$ni][$nj];
                if ($cell === 'X' || $cell === 'D') continue;
                if ($water[$ni][$nj] > $water[$x][$y] + 1) {
                    $water[$ni][$nj] = $water[$x][$y] + 1;
                    $wq[] = [$ni, $nj];
                }
            }
        }
        $dist = array_fill(0, $m, array_fill(0, $n, -1));
        $q = [[$sx, $sy]];
        $dist[$sx][$sy] = 0;
        for ($h = 0; $h < count($q); $h++) {
            $x = $q[$h][0];
            $y = $q[$h][1];
            if ($x === $dx && $y === $dy) return $dist[$x][$y];
            foreach ($dirs as $d) {
                $ni = $x + $d[0];
                $nj = $y + $d[1];
                if ($ni < 0 || $nj < 0 || $ni >= $m || $nj >= $n || $dist[$ni][$nj] !== -1) continue;
                if ($land[$ni][$nj] === 'X') continue;
                $nd = $dist[$x][$y] + 1;
                if ($land[$ni][$nj] !== 'D' && $nd >= $water[$ni][$nj]) continue;
                $dist[$ni][$nj] = $nd;
                $q[] = [$ni, $nj];
            }
        }
        return -1;
    }
}
