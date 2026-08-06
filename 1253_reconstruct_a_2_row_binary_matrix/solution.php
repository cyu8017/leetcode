<?php
// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

class Solution {
    /**
     * @param Integer $upper
     * @param Integer $lower
     * @param Integer[] $colsum
     * @return Integer[][]
     */
    function reconstructMatrix($upper, $lower, $colsum) {
        $len = count($colsum);
        $top = array_fill(0, $len, 0);
        $bottom = array_fill(0, $len, 0);
        for ($i = 0; $i < $len; $i++) {
            if ($colsum[$i] === 2) {
                $top[$i] = $bottom[$i] = 1;
                $upper--; $lower--;
            }
        }
        if ($upper < 0 || $lower < 0) return [];
        for ($i = 0; $i < $len; $i++) {
            if ($colsum[$i] === 1) {
                if ($upper > 0) { $top[$i] = 1; $upper--; }
                elseif ($lower > 0) { $bottom[$i] = 1; $lower--; }
                else return [];
            }
        }
        return ($upper === 0 && $lower === 0) ? [$top, $bottom] : [];
    }
}
