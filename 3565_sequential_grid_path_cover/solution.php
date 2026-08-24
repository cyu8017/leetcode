<?php
// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

class Solution {
    private $grid;
    private $m;
    private $n;
    private $dirs;
    private $st;
    private $path;

    private function f($i, $j) {
        return $i * $this->n + $j;
    }

    private function dfs($i, $j, $v) {
        $this->path[] = [$i, $j];
        if (count($this->path) === $this->m * $this->n) return true;
        $idx = $this->f($i, $j);
        $this->st |= 1 << $idx;
        if ($this->grid[$i][$j] === $v) $v++;
        for ($t = 0; $t < 4; $t++) {
            $x = $i + $this->dirs[$t];
            $y = $j + $this->dirs[$t + 1];
            if (0 <= $x && $x < $this->m && 0 <= $y && $y < $this->n) {
                $idx2 = $this->f($x, $y);
                if ((($this->st >> $idx2) & 1) === 0 && ($this->grid[$x][$y] === 0 || $this->grid[$x][$y] === $v)) {
                    if ($this->dfs($x, $y, $v)) return true;
                }
            }
        }
        array_pop($this->path);
        $this->st ^= 1 << $idx;
        return false;
    }

    function findPath($grid, $k) {
        $this->grid = $grid;
        $this->m = count($grid);
        $this->n = count($grid[0]);
        $this->dirs = [-1, 0, 1, 0, -1];
        $this->st = 0;
        $this->path = [];
        for ($i = 0; $i < $this->m; $i++) {
            for ($j = 0; $j < $this->n; $j++) {
                if ($grid[$i][$j] === 0 || $grid[$i][$j] === 1) {
                    if ($this->dfs($i, $j, 1)) return $this->path;
                    $this->path = [];
                    $this->st = 0;
                }
            }
        }
        return [];
    }
}
