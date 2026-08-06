<?php
class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function maxMatrixSum($matrix) {
        $total = 0;
        $neg = 0;
        $mn = PHP_INT_MAX;
        foreach ($matrix as $row) {
            foreach ($row as $x) {
                if ($x < 0) {
                    $neg++;
                }
                $ax = abs($x);
                $total += $ax;
                if ($ax < $mn) {
                    $mn = $ax;
                }
            }
        }
        if ($neg % 2 === 0) {
            return $total;
        }
        return $total - 2 * $mn;
    }
}
