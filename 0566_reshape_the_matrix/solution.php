<?php
// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

class Solution {
    function matrixReshape($mat, $r, $c) {
        $rows = count($mat);
        $cols = count($mat[0]);
        if ($rows * $cols !== $r * $c) return $mat;
        $result = [];
        for ($i = 0; $i < $r; ++$i) $result[$i] = array_fill(0, $c, 0);
        $index = 0;
        for ($i = 0; $i < $r; ++$i) {
            for ($j = 0; $j < $c; ++$j) {
                $result[$i][$j] = $mat[intdiv($index, $cols)][$index % $cols];
                ++$index;
            }
        }
        return $result;
    }
}
