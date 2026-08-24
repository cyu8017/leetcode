<?php
// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

class Solution {
    function isToeplitzMatrix($matrix) {
        for ($r = 1; $r < count($matrix); $r++) {
            for ($c = 1; $c < count($matrix[0]); $c++) {
                if ($matrix[$r][$c] !== $matrix[$r - 1][$c - 1]) return false;
            }
        }
        return true;
    }
}
