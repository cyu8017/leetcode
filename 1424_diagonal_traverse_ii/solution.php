<?php
class Solution {
    function findDiagonalOrder($nums) {
        $diagonals = [];
        foreach ($nums as $row => $values) {
            foreach ($values as $col => $value) {
                $diagonals[$row + $col][] = $value;
            }
        }
        ksort($diagonals);
        $answer = [];
        foreach ($diagonals as $values) {
            for ($i = count($values) - 1; $i >= 0; $i--) $answer[] = $values[$i];
        }
        return $answer;
    }
}
