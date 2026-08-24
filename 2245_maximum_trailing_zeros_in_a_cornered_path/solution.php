<?php
// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

class Solution {
    function maxTrailingZeros($grid) {
        $fact = function($x) {
            $t = 0;
            $f = 0;
            while ($x % 2 === 0) { $t++; $x = intdiv($x, 2); }
            while ($x % 5 === 0) { $f++; $x = intdiv($x, 5); }
            return [$t, $f];
        };
        $m = count($grid);
        $n = count($grid[0]);
        $left2 = [];
        $left5 = [];
        $up2 = [];
        $up5 = [];
        for ($i = 0; $i < $m; $i++) {
            $left2[$i] = array_fill(0, $n, 0);
            $left5[$i] = array_fill(0, $n, 0);
            $up2[$i] = array_fill(0, $n, 0);
            $up5[$i] = array_fill(0, $n, 0);
        }
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $p = $fact($grid[$i][$j]);
                $left2[$i][$j] = $up2[$i][$j] = $p[0];
                $left5[$i][$j] = $up5[$i][$j] = $p[1];
                if ($j > 0) {
                    $left2[$i][$j] += $left2[$i][$j - 1];
                    $left5[$i][$j] += $left5[$i][$j - 1];
                }
                if ($i > 0) {
                    $up2[$i][$j] += $up2[$i - 1][$j];
                    $up5[$i][$j] += $up5[$i - 1][$j];
                }
            }
        }
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $cell = $fact($grid[$i][$j]);
                $L2 = $left2[$i][$j];
                $L5 = $left5[$i][$j];
                $R2 = $left2[$i][$n - 1] - $left2[$i][$j] + $cell[0];
                $R5 = $left5[$i][$n - 1] - $left5[$i][$j] + $cell[1];
                $U2 = $up2[$i][$j];
                $U5 = $up5[$i][$j];
                $D2 = $up2[$m - 1][$j] - $up2[$i][$j] + $cell[0];
                $D5 = $up5[$m - 1][$j] - $up5[$i][$j] + $cell[1];
                $cands = [
                    [$L2 + $U2 - $cell[0], $L5 + $U5 - $cell[1]],
                    [$L2 + $D2 - $cell[0], $L5 + $D5 - $cell[1]],
                    [$R2 + $U2 - $cell[0], $R5 + $U5 - $cell[1]],
                    [$R2 + $D2 - $cell[0], $R5 + $D5 - $cell[1]],
                ];
                foreach ($cands as $ab) $ans = max($ans, min($ab[0], $ab[1]));
            }
        }
        return $ans;
    }
}
