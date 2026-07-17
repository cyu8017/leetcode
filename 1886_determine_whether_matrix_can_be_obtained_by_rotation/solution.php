<?php
// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution {
    /**
     * @param Integer[][] $mat
     * @param Integer[][] $target
     * @return Boolean
     */
    function findRotation($mat, $target) {
        $current = $mat;
        for ($rotation = 0; $rotation < 4; $rotation++) {
            if ($current === $target) {
                return true;
            }
            $n = count($current);
            $rotated = [];
            for ($col = 0; $col < $n; $col++) {
                $rowValues = [];
                for ($row = 0; $row < $n; $row++) {
                    $rowValues[] = $current[$n - 1 - $row][$col];
                }
                $rotated[] = $rowValues;
            }
            $current = $rotated;
        }
        return false;
    }
}
