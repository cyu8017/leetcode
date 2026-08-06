<?php
class Solution {
    function maxNumberOfFamilies($n, $reservedSeats) {
        $rows = [];
        foreach ($reservedSeats as [$r, $c]) {
            if ($c >= 2 && $c <= 9) $rows[$r] = ($rows[$r] ?? 0) | (1 << ($c - 2));
        }
        $ans = 2 * ($n - count($rows));
        foreach ($rows as $m) {
            $left = ($m & 0b00001111) === 0;
            $right = ($m & 0b11110000) === 0;
            $middle = ($m & 0b00111100) === 0;
            $ans += ($left && $right) ? 2 : (($left || $right || $middle) ? 1 : 0);
        }
        return $ans;
    }
}
