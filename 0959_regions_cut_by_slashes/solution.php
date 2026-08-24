<?php
// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

class Solution {
    function regionsBySlashes($grid) {
        $n = count($grid);
        $parent = range(0, $n * $n * 4 - 1);
        $find = function ($x) use (&$find, &$parent) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        for ($r = 0; $r < $n; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $root = 4 * ($r * $n + $c);
                $ch = $grid[$r][$c];
                if ($ch === "/") {
                    $parent[$find($root + 0)] = $find($root + 3);
                    $parent[$find($root + 1)] = $find($root + 2);
                } elseif ($ch === "\\") {
                    $parent[$find($root + 0)] = $find($root + 1);
                    $parent[$find($root + 2)] = $find($root + 3);
                } else {
                    $parent[$find($root + 0)] = $find($root + 1);
                    $parent[$find($root + 1)] = $find($root + 2);
                    $parent[$find($root + 2)] = $find($root + 3);
                }
                if ($r + 1 < $n) $parent[$find($root + 2)] = $find($root + 4 * $n + 0);
                if ($c + 1 < $n) $parent[$find($root + 1)] = $find($root + 4 + 3);
            }
        }
        $ans = 0;
        $len = count($parent);
        for ($i = 0; $i < $len; $i++) if ($find($i) === $i) $ans++;
        return $ans;
    }
}
