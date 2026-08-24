<?php
// LeetCode 2128 - Remove All Ones With Row and Column Flips
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Boolean
     */
    function removeOnes($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        for ($i = 1; $i < $m; $i++) {
            $same = $grid[$i][0] === $grid[0][0];
            for ($j = 0; $j < $n; $j++) {
                if (($grid[$i][$j] === $grid[0][$j]) !== $same) return false;
            }
        }
        return true;
    }
}
