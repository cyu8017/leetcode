<?php
// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

class Solution {
    /**
     * @param CustomFunction $customfunction
     * @param Integer $z
     * @return Integer[][]
     */
    function findSolution($customfunction, $z) {
        $answer = [];
        $x = 1; $y = 1000;
        while ($x <= 1000 && $y >= 1) {
            $value = $customfunction->f($x, $y);
            if ($value === $z) {
                $answer[] = [$x, $y];
                $x++; $y--;
            } elseif ($value < $z) $x++;
            else $y--;
        }
        return $answer;
    }
}
