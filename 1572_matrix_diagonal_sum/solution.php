<?php

class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function diagonalSum($mat) {
        $n = count($mat);
        $sum = 0;
        for ($i = 0; $i < $n; $i++) {
            $sum += $mat[$i][$i] + $mat[$i][$n - 1 - $i];
        }
        if ($n % 2 === 1) {
            $sum -= $mat[intdiv($n, 2)][intdiv($n, 2)];
        }
        return $sum;
    }
}
