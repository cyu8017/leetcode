<?php
// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

class NeighborSum {
    private $grid;
    private $d;
    private $dirs;

    function __construct($grid) {
        $this->grid = $grid;
        $this->d = [];
        $this->dirs = [
            [-1, 0, 1, 0, -1],
            [-1, 1, 1, -1, -1]
        ];
        for ($i = 0; $i < count($grid); $i++) {
            for ($j = 0; $j < count($grid[$i]); $j++) {
                $this->d[$grid[$i][$j]] = [$i, $j];
            }
        }
    }

    function cal($value, $k) {
        $p = $this->d[$value];
        $s = 0;
        for ($q = 0; $q < 4; $q++) {
            $x = $p[0] + $this->dirs[$k][$q];
            $y = $p[1] + $this->dirs[$k][$q + 1];
            if ($x >= 0 && $x < count($this->grid) && $y >= 0 && $y < count($this->grid[0])) $s += $this->grid[$x][$y];
        }
        return $s;
    }

    function adjacentSum($value) {
        return $this->cal($value, 0);
    }

    function diagonalSum($value) {
        return $this->cal($value, 1);
    }
}
