<?php
// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

class Solution {
    /**
     * @param String[][] $boxGrid
     * @return String[][]
     */
    function rotateTheBox($boxGrid) {
        $m = count($boxGrid);
        $n = count($boxGrid[0]);
        $rotated = array_fill(0, $n, array_fill(0, $m, '.'));

        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $m; $j++) {
                $rotated[$i][$j] = $boxGrid[$m - 1 - $j][$i];
            }
        }

        for ($col = 0; $col < $m; $col++) {
            $row = $n - 1;
            for ($i = $n - 1; $i >= 0; $i--) {
                if ($rotated[$i][$col] === '*') {
                    $row = $i - 1;
                } elseif ($rotated[$i][$col] === '#') {
                    $rotated[$i][$col] = '.';
                    $rotated[$row][$col] = '#';
                    $row--;
                }
            }
        }

        return $rotated;
    }
}
