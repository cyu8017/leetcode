<?php
// LeetCode 0074 - Search a 2D Matrix
// https://leetcode.com/problems/search-a-2d-matrix/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @param Integer $target
     * @return Boolean
     */
    function searchMatrix($matrix, $target) {
        $row = 0;
        $col = count($matrix[0]) - 1;

        while ($row < count($matrix) && $col >= 0) {
            if ($matrix[$row][$col] === $target) {
                return true;
            }
            if ($matrix[$row][$col] > $target) {
                $col--;
            } else {
                $row++;
            }
        }

        return false;
    }
}
