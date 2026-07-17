<?php
// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

class Solution {
    /**
     * @param String[] $grid
     * @param Integer $catJump
     * @param Integer $mouseJump
     * @return Boolean
     */
    function canMouseWin($grid, $catJump, $mouseJump) {
        $rows = count($grid);
        $cols = strlen($grid[0]);
        $totalOpen = 0;
        $mouse = 0;
        $cat = 0;
        $food = 0;
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                $cell = $grid[$r][$c];
                if ($cell !== '#') {
                    $totalOpen++;
                }
                if ($cell === 'M') {
                    $mouse = $r * $cols + $c;
                } elseif ($cell === 'C') {
                    $cat = $r * $cols + $c;
                } elseif ($cell === 'F') {
                    $food = $r * $cols + $c;
                }
            }
        }
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $computeMoves = function ($pos, $jump) use ($grid, $rows, $cols, $dirs) {
            $r = intdiv($pos, $cols);
            $c = $pos % $cols;
            $out = [$pos];
            foreach ($dirs as [$dr, $dc]) {
                for ($step = 1; $step <= $jump; $step++) {
                    $nr = $r + $dr * $step;
                    $nc = $c + $dc * $step;
                    if ($nr < 0 || $nr >= $rows || $nc < 0 || $nc >= $cols || $grid[$nr][$nc] === '#') {
                        break;
                    }
                    $out[] = $nr * $cols + $nc;
                }
            }
            return $out;
        };
        $cells = $rows * $cols;
        $mouseMoves = [];
        $catMoves = [];
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                if ($grid[$r][$c] !== '#') {
                    $pos = $r * $cols + $c;
                    $mouseMoves[$pos] = $computeMoves($pos, $mouseJump);
                    $catMoves[$pos] = $computeMoves($pos, $catJump);
                }
            }
        }
        $maxTurn = 2 * $totalOpen;
        $memo = [];
        $win = function ($m, $c, $turn) use (
            &$win, $food, $maxTurn, $cells, $mouseMoves, $catMoves, &$memo
        ) {
            if ($turn >= $maxTurn) {
                return false;
            }
            if ($m === $food) {
                return true;
            }
            if ($c === $food || $c === $m) {
                return false;
            }
            $key = ($m * $cells + $c) * $maxTurn + $turn;
            if (isset($memo[$key])) {
                return $memo[$key];
            }
            if ($turn % 2 === 0) {
                $result = false;
                foreach ($mouseMoves[$m] as $nm) {
                    if ($win($nm, $c, $turn + 1)) {
                        $result = true;
                        break;
                    }
                }
            } else {
                $result = true;
                foreach ($catMoves[$c] as $nc) {
                    if (!$win($m, $nc, $turn + 1)) {
                        $result = false;
                        break;
                    }
                }
            }
            $memo[$key] = $result;
            return $result;
        };
        return $win($mouse, $cat, 0);
    }
}
