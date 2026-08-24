<?php
// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

class Solution {
    function maxPathSum($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $answer = -2147483648;
        for ($row = 0; $row < $rows; $row++) {
            $r = $row;
            $answer = max($answer, $this->checkLine($cols, function ($col) use ($grid, $r) {
                return $grid[$r][$col];
            }));
        }
        for ($col = 0; $col < $cols; $col++) {
            $c = $col;
            $answer = max($answer, $this->checkLine($rows, function ($row) use ($grid, $c) {
                return $grid[$row][$c];
            }));
        }
        for ($row = 1; $row + 1 < $rows; $row++) {
            for ($col = 1; $col + 1 < $cols; $col++) {
                if ($grid[$row][$col] > $answer) $answer = $grid[$row][$col];
            }
        }
        return $answer;
    }

    private function checkLine($length, $value) {
        $answer = -2147483648;
        $bestEnding = $value(0) + $value(1);
        if ($bestEnding > $answer) $answer = $bestEnding;
        for ($i = 2; $i < $length; $i++) {
            if ($value($i - 1) + $value($i) > $bestEnding + $value($i)) $bestEnding = $value($i - 1) + $value($i);
            else $bestEnding += $value($i);
            if ($bestEnding > $answer) $answer = $bestEnding;
        }
        return $answer;
    }
}
