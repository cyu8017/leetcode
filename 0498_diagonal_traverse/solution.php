<?php
// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer[]
     */
    function findDiagonalOrder($mat) {
        return $this->find_diagonal_order($mat);
    }

    /**
     * @param Integer[][] $mat
     * @return Integer[]
     */
    function find_diagonal_order($mat) {
        if ($mat === [] || $mat[0] === []) {
            return [];
        }
        $rows = count($mat);
        $cols = count($mat[0]);
        $result = [];
        $row = 0;
        $col = 0;
        $upward = true;

        for ($count = 0; $count < $rows * $cols; $count++) {
            $result[] = $mat[$row][$col];
            if ($upward) {
                if ($col === $cols - 1) {
                    $row++;
                    $upward = false;
                } elseif ($row === 0) {
                    $col++;
                    $upward = false;
                } else {
                    $row--;
                    $col++;
                }
            } elseif ($row === $rows - 1) {
                $col++;
                $upward = true;
            } elseif ($col === 0) {
                $row++;
                $upward = true;
            } else {
                $row++;
                $col--;
            }
        }
        return $result;
    }
}
