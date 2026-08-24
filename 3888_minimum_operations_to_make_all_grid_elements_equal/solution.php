<?php
// LeetCode 3888 - Minimum Operations to Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

class Solution {
    public $grid;
    public $k;
    public $m;
    public $n;
    function check($target) {
        $diff = [];
        for ($i = 0; $i < $this->m + 2; $i++) $diff[$i] = array_fill(0, $this->n + 2, 0);
        $totalOps = 0;
        for ($i = 1; $i <= $this->m; $i++) {
            for ($j = 1; $j <= $this->n; $j++) {
                $diff[$i][$j] += $diff[$i - 1][$j] + $diff[$i][$j - 1] - $diff[$i - 1][$j - 1];
                $curVal = $this->grid[$i - 1][$j - 1] + $diff[$i][$j];
                if ($curVal > $target) return -1;
                if ($curVal < $target) {
                    if ($i + $this->k - 1 > $this->m || $j + $this->k - 1 > $this->n) return -1;
                    $needed = $target - $curVal;
                    $totalOps += $needed;
                    $diff[$i][$j] += $needed;
                    $diff[$i + $this->k][$j] -= $needed;
                    $diff[$i][$j + $this->k] -= $needed;
                    $diff[$i + $this->k][$j + $this->k] += $needed;
                }
            }
        }
        return $totalOps;
    }
    function minOperations($grid, $k) {
        $this->grid = $grid;
        $this->k = $k;
        $this->m = count($grid);
        $this->n = count($grid[0]);
        $maxVal = $grid[0][0];
        foreach ($grid as $row) foreach ($row as $x) $maxVal = max($maxVal, $x);
        for ($t = $maxVal; $t <= $maxVal + 1; $t++) {
            $res = $this->check($t);
            if ($res !== -1) return $res;
        }
        return -1;
    }
}
