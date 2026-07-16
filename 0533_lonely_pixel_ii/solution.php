<?php
// LeetCode 0533 - Lonely Pixel II
// https://leetcode.com/problems/lonely-pixel-ii/

class Solution {
    /**
     * @param String[][] $picture
     * @param Integer $target
     * @return Integer
     */
    function findBlackPixel($picture, $target) {
        return $this->find_black_pixel($picture, $target);
    }

    /**
     * @param String[][] $picture
     * @param Integer $target
     * @return Integer
     */
    function find_black_pixel($picture, $target) {
        $rows = count($picture);
        $cols = count($picture[0]);
        $rowStrings = array_map(function ($row) {
            return implode("", $row);
        }, $picture);
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
            if ($rowCounts[$r] !== $target) {
                continue;
            }
            for ($c = 0; $c < $cols; $c++) {
                if ($picture[$r][$c] !== "B" || $colCounts[$c] !== $target) {
                    continue;
                }
                $matches = true;
                for ($i = 0; $i < $rows; $i++) {
                    if ($picture[$i][$c] === "B" && $rowStrings[$r] !== $rowStrings[$i]) {
                        $matches = false;
                        break;
                    }
                }
                if ($matches) {
                    $lonely++;
                }
            }
        }
        return $lonely;
    }
}
