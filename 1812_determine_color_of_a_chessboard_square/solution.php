<?php
// LeetCode 1812 - Determine Color of a Chessboard Square
// https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution {
    /**
     * @param String $coordinates
     * @return Boolean
     */
    function squareIsWhite($coordinates) {
        $col = ord($coordinates[0]) - ord('a') + 1;
        $row = (int)$coordinates[1];
        return ($col + $row) % 2 === 1;
    }
}
