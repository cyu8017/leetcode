<?php
// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

class Solution {
    private static $g = null;

    function minDifference($n, $k) {
        $MX = 100001;
        if (self::$g === null) {
            $g = array_fill(0, $MX, []);
            for ($i = 1; $i < $MX; $i++)
                for ($j = $i; $j < $MX; $j += $i) $g[$j][] = $i;
            self::$g = $g;
        }
        $g = self::$g;
        $cur = PHP_INT_MAX;
        $ans = [];
        $path = array_fill(0, $k, 0);
        $dfs = function($i, $x, $mi, $mx) use (&$dfs, &$cur, &$ans, &$path, $g) {
            if ($i === 0) {
                $d = max($mx, $x) - min($mi, $x);
                if ($d < $cur) {
                    $cur = $d;
                    $path[$i] = $x;
                    $ans = $path;
                }
                return;
            }
            foreach ($g[$x] as $y) {
                $path[$i] = $y;
                $dfs($i - 1, intdiv($x, $y), min($mi, $y), max($mx, $y));
            }
        };
        $dfs($k - 1, $n, PHP_INT_MAX, 0);
        return $ans;
    }
}
