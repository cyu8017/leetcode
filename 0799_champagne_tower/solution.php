<?php
// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

class Solution {
    /**
     * @param Integer $poured
     * @param Integer $query_row
     * @param Integer $query_glass
     * @return Float
     */
    function champagneTower($poured, $query_row, $query_glass) {
        $row = [$poured];
        for ($r = 0; $r < $query_row; $r++) {
            $nextRow = array_fill(0, $r + 2, 0.0);
            $len = count($row);
            for ($i = 0; $i < $len; $i++) {
                $overflow = ($row[$i] - 1.0) / 2.0;
                if ($overflow > 0) {
                    $nextRow[$i] += $overflow;
                    $nextRow[$i + 1] += $overflow;
                }
            }
            $row = $nextRow;
        }
        return min(1.0, $row[$query_glass]);
    }
}
