<?php

class Solution {
    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function numSpecial($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $rows = array_fill(0, $m, 0);
        $cols = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $rows[$i] += $mat[$i][$j];
                $cols[$j] += $mat[$i][$j];
            }
        }
        $answer = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($mat[$i][$j] === 1 && $rows[$i] === 1 && $cols[$j] === 1) {
                    $answer++;
                }
            }
        }
        return $answer;
    }
}
