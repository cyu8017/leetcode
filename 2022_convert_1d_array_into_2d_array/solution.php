<?php
// LeetCode 2022 - Convert 1D Array Into 2D Array
// https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution {
    /**
     * @param Integer[] $original
     * @param Integer $m
     * @param Integer $n
     * @return Integer[][]
     */
    function construct2DArray($original, $m, $n) {
        if (count($original) !== $m * $n) return [];
        $ans = [];
        for ($i = 0; $i < $m; $i++) {
            $ans[$i] = [];
            for ($j = 0; $j < $n; $j++) $ans[$i][$j] = $original[$i * $n + $j];
        }
        return $ans;
    }
}
