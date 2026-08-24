<?php
// LeetCode 3197 - Find the Minimum Area to Cover All Ones II
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

class Solution {
    private $grid;

    function minimumSum($grid) {
        $this->grid = $grid;
        $m = count($grid);
        $n = count($grid[0]);
        $ans = $m * $n;
        for ($i1 = 0; $i1 < $m - 1; $i1++) {
            for ($i2 = $i1 + 1; $i2 < $m - 1; $i2++) {
                $ans = min($ans, $this->area(0, 0, $i1, $n - 1) + $this->area($i1 + 1, 0, $i2, $n - 1) + $this->area($i2 + 1, 0, $m - 1, $n - 1));
            }
        }
        for ($j1 = 0; $j1 < $n - 1; $j1++) {
            for ($j2 = $j1 + 1; $j2 < $n - 1; $j2++) {
                $ans = min($ans, $this->area(0, 0, $m - 1, $j1) + $this->area(0, $j1 + 1, $m - 1, $j2) + $this->area(0, $j2 + 1, $m - 1, $n - 1));
            }
        }
        for ($i = 0; $i < $m - 1; $i++) {
            for ($j = 0; $j < $n - 1; $j++) {
                $ans = min($ans, $this->area(0, 0, $i, $j) + $this->area(0, $j + 1, $i, $n - 1) + $this->area($i + 1, 0, $m - 1, $n - 1));
                $ans = min($ans, $this->area(0, 0, $i, $n - 1) + $this->area($i + 1, 0, $m - 1, $j) + $this->area($i + 1, $j + 1, $m - 1, $n - 1));
                $ans = min($ans, $this->area(0, 0, $i, $j) + $this->area($i + 1, 0, $m - 1, $j) + $this->area(0, $j + 1, $m - 1, $n - 1));
                $ans = min($ans, $this->area(0, 0, $m - 1, $j) + $this->area(0, $j + 1, $i, $n - 1) + $this->area($i + 1, $j + 1, $m - 1, $n - 1));
            }
        }
        return $ans;
    }

    private function area($i1, $j1, $i2, $j2) {
        $inf = 1000000000;
        $x1 = $inf;
        $y1 = $inf;
        $x2 = -$inf;
        $y2 = -$inf;
        for ($i = $i1; $i <= $i2; $i++) {
            for ($j = $j1; $j <= $j2; $j++) {
                if ($this->grid[$i][$j] === 1) {
                    $x1 = min($x1, $i);
                    $y1 = min($y1, $j);
                    $x2 = max($x2, $i);
                    $y2 = max($y2, $j);
                }
            }
        }
        if ($x1 === $inf) return 0;
        return ($x2 - $x1 + 1) * ($y2 - $y1 + 1);
    }
}
