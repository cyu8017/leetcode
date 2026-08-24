<?php
// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

class Solution {
    function countLocalMaximums($matrix) {
        $rows = count($matrix);
        $cols = count($matrix[0]);
        $positions = array_fill(0, 201, []);
        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                $value = $matrix[$row][$col];
                if ($value > 0) $positions[$value][] = [$row, $col];
            }
        }
        $answer = 0;
        for ($value = 1; $value <= 200; $value++) {
            if (count($positions[$value]) === 0) continue;
            $prefix = array_fill(0, $rows + 1, array_fill(0, $cols + 1, 0));
            for ($row = 0; $row < $rows; $row++) {
                for ($col = 0; $col < $cols; $col++) {
                    $add = $matrix[$row][$col] > $value ? 1 : 0;
                    $prefix[$row + 1][$col + 1] = $prefix[$row][$col + 1] + $prefix[$row + 1][$col] - $prefix[$row][$col] + $add;
                }
            }
            foreach ($positions[$value] as $pos) {
                $row = $pos[0];
                $col = $pos[1];
                $top = max(0, $row - $value);
                $bottom = min($rows - 1, $row + $value);
                $left = max(0, $col - $value);
                $right = min($cols - 1, $col + $value);
                $greater = $prefix[$bottom + 1][$right + 1] - $prefix[$top][$right + 1] - $prefix[$bottom + 1][$left] + $prefix[$top][$left];
                foreach ([-$value, $value] as $dr) {
                    foreach ([-$value, $value] as $dc) {
                        $rr = $row + $dr;
                        $cc = $col + $dc;
                        if ($rr >= 0 && $rr < $rows && $cc >= 0 && $cc < $cols && $matrix[$rr][$cc] > $value) $greater--;
                    }
                }
                if ($greater == 0) $answer++;
            }
        }
        return $answer;
    }
}
