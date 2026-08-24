<?php
// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer[][] $hits
     * @return Integer[]
     */
    function hitBricks($grid, $hits) {
        $m = count($grid);
        $n = count($grid[0]);
        $roof = $m * $n;
        $parent = [];
        $size = [];
        for ($i = 0; $i <= $roof; $i++) {
            $parent[$i] = $i;
            $size[$i] = 1;
        }
        $find = function($x) use (&$parent) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $unite = function($a, $b) use (&$parent, &$size, $find) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra === $rb) return;
            $parent[$ra] = $rb;
            $size[$rb] += $size[$ra];
        };
        $idx = function($r, $c) use ($n) { return $r * $n + $c; };
        $status = [];
        foreach ($grid as $row) $status[] = $row;
        foreach ($hits as $hit) $status[$hit[0]][$hit[1]] = 0;
        $dr = [-1, 1, 0, 0];
        $dc = [0, 0, -1, 1];
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($status[$r][$c] === 0) continue;
                if ($r === 0) $unite($idx($r, $c), $roof);
                for ($k = 0; $k < 4; $k++) {
                    $nr = $r + $dr[$k];
                    $nc = $c + $dc[$k];
                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $status[$nr][$nc] === 1) {
                        $unite($idx($r, $c), $idx($nr, $nc));
                    }
                }
            }
        }
        $answer = array_fill(0, count($hits), 0);
        for ($i = count($hits) - 1; $i >= 0; $i--) {
            $r = $hits[$i][0];
            $c = $hits[$i][1];
            if ($grid[$r][$c] === 0) continue;
            $prev = $size[$find($roof)];
            $status[$r][$c] = 1;
            if ($r === 0) $unite($idx($r, $c), $roof);
            for ($k = 0; $k < 4; $k++) {
                $nr = $r + $dr[$k];
                $nc = $c + $dc[$k];
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $status[$nr][$nc] === 1) {
                    $unite($idx($r, $c), $idx($nr, $nc));
                }
            }
            $curr = $size[$find($roof)];
            $answer[$i] = max(0, $curr - $prev - 1);
        }
        return $answer;
    }
}
