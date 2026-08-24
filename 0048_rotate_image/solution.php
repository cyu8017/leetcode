<?php
// LeetCode 0048 - Rotate Image
// https://leetcode.com/problems/rotate-image/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return void
     */
    function rotate(&$matrix) {
        $n = count($matrix);

        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $tmp = $matrix[$i][$j];
                $matrix[$i][$j] = $matrix[$j][$i];
                $matrix[$j][$i] = $tmp;
            }
        }

        foreach ($matrix as &$row) {
            $row = array_reverse($row);
        }
        unset($row);
    }
}
