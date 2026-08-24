<?php
// LeetCode 0240 - Search a 2D Matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @param Integer $target
     * @return Boolean
     */
    function searchMatrix($matrix, $target) {
        if (empty($matrix) || empty($matrix[0])) {
            return false;
        }
        $row = 0;
        $col = count($matrix[0]) - 1;
        while ($row < count($matrix) && $col >= 0) {
            $value = $matrix[$row][$col];
            if ($value == $target) {
                return true;
            }
            if ($value > $target) {
                $col--;
            } else {
                $row++;
            }
        }
        return false;
    }
}
