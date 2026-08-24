<?php
// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

class Solution {
    function sortMatrix($grid) {
        $n = count($grid);
        $diags = [];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $key = $i - $j;
                if (!isset($diags[$key])) $diags[$key] = [];
                $diags[$key][] = $grid[$i][$j];
            }
        }
        foreach ($diags as $key => &$list) {
            if ($key >= 0) rsort($list);
            else sort($list);
        }
        unset($list);
        $idx = [];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $k = $i - $j;
                $pos = $idx[$k] ?? 0;
                $grid[$i][$j] = $diags[$k][$pos];
                $idx[$k] = $pos + 1;
            }
        }
        return $grid;
    }
}
