<?php
// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

class Solution {
    /**
     * @param String[][] $picture
     * @return Integer
     */
    function findLonelyPixel($picture) {
        return $this->find_lonely_pixel($picture);
    }

    /**
     * @param String[][] $picture
     * @return Integer
     */
    function find_lonely_pixel($picture) {
        $rows = count($picture);
        $cols = count($picture[0]);
        $rowCounts = array_map(function ($row) {
            return count(array_filter($row, function ($cell) {
                return $cell === "B";
            }));
        }, $picture);

        $colCounts = [];
        for ($c = 0; $c < $cols; $c++) {
            $count = 0;
            for ($r = 0; $r < $rows; $r++) {
                if ($picture[$r][$c] === "B") {
                    $count++;
                }
            }
            $colCounts[] = $count;
        }

        $lonely = 0;
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                if ($picture[$r][$c] === "B" && $rowCounts[$r] === 1 && $colCounts[$c] === 1) {
                    $lonely++;
                }
            }
        }
        return $lonely;
    }
}
