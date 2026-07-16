<?php
// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer[][]
     */
    function updateMatrix($mat) {
        $rows = count($mat);
        $cols = count($mat[0]);
        $dist = array_fill(0, $rows, array_fill(0, $cols, 1000000000));
        $queue = [];

        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                if ($mat[$row][$col] === 0) {
                    $dist[$row][$col] = 0;
                    $queue[] = [$row, $col];
                }
            }
        }

        $directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (!empty($queue)) {
            [$row, $col] = array_shift($queue);
            foreach ($directions as [$dr, $dc]) {
                $nr = $row + $dr;
                $nc = $col + $dc;
                if ($nr < 0 || $nr >= $rows || $nc < 0 || $nc >= $cols) {
                    continue;
                }
                $candidate = $dist[$row][$col] + 1;
                if ($dist[$nr][$nc] > $candidate) {
                    $dist[$nr][$nc] = $candidate;
                    $queue[] = [$nr, $nc];
                }
            }
        }

        return $dist;
    }
}
