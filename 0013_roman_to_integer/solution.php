<?php
// LeetCode 0013 - Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function romanToInt($s) {
        $values = ['I' => 1, 'V' => 5, 'X' => 10, 'L' => 50, 'C' => 100, 'D' => 500, 'M' => 1000];
        $total = 0;
        $prev = 0;

        for ($i = strlen($s) - 1; $i >= 0; $i--) {
            $curr = $values[$s[$i]];
            if ($curr < $prev) {
                $total -= $curr;
            } else {
                $total += $curr;
            }
            $prev = $curr;
        }

        return $total;
    }
}
