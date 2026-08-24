<?php
// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

class Solution {
    function constructGridLayout($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $deg = [];
        for ($i = 0; $i < $n; $i++) $deg[$i] = count($g[$i]);
        $start = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($deg[$i] === 1) { $start = $i; break; }
            if ($deg[$i] === 2) $start = $i;
        }
        $vis = array_fill(0, $n, false);
        $row = [];
        $cur = $start;
        $prev = -1;
        for (;;) {
            $row[] = $cur;
            $vis[$cur] = true;
            $next = -1;
            foreach ($g[$cur] as $v) {
                if ($v !== $prev && !$vis[$v] && $deg[$v] <= 3) {
                    $next = $v;
                    if ($deg[$v] < 4) break;
                }
            }
            if ($next === -1) break;
            $prev = $cur;
            $cur = $next;
        }
        $width = count($row);
        $height = $width !== 0 ? intdiv($n, $width) : $n;
        if ($width === 0 || $width * $height !== $n) {
            for ($w = 1; $w <= $n; $w++) {
                if ($n % $w === 0) { $width = $w; $height = intdiv($n, $w); break; }
            }
        }
        $grid = [];
        for ($i = 0; $i < $height; $i++) $grid[$i] = array_fill(0, $width, 0);
        for ($i = 0; $i < $n; $i++) $grid[intdiv($i, $width)][$i % $width] = $i;
        return $grid;
    }
}
