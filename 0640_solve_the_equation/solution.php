<?php
// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

class Solution {
    function solveEquation($equation) {
        $parse = function($expr) {
            $coef = 0;
            $constant = 0;
            $n = strlen($expr);
            $i = 0;
            while ($i < $n) {
                $sign = 1;
                if ($expr[$i] === "+" || $expr[$i] === "-") {
                    $sign = $expr[$i] === "-" ? -1 : 1;
                    ++$i;
                }
                $value = 0;
                $hasDigit = false;
                while ($i < $n && $expr[$i] >= "0" && $expr[$i] <= "9") {
                    $hasDigit = true;
                    $value = $value * 10 + (ord($expr[$i]) - 48);
                    ++$i;
                }
                if ($i < $n && $expr[$i] === "x") {
                    $coef += $sign * ($hasDigit ? $value : 1);
                    ++$i;
                } else {
                    $constant += $sign * $value;
                }
            }
            return [$coef, $constant];
        };
        $eq = strpos($equation, "=");
        $left = $parse(substr($equation, 0, $eq));
        $right = $parse(substr($equation, $eq + 1));
        $coef = $left[0] - $right[0];
        $constant = $right[1] - $left[1];
        if ($coef === 0) return $constant === 0 ? "Infinite solutions" : "No solution";
        return "x=" . intdiv($constant, $coef);
    }
}
