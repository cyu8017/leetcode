<?php
// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

class Solution {
    /**
     * @param String $expression
     * @return Integer
     */
    function minOperationsToFlip($expression) {
        $combine = function ($left, $op, $right) {
            [$leftVal, $leftToZero, $leftToOne] = $left;
            [$rightVal, $rightToZero, $rightToOne] = $right;
            if ($op === '&') {
                $andVal = $leftVal & $rightVal;
                $andToZero = min($leftToZero, $leftToOne + $rightToZero);
                $andToOne = $leftToOne + $rightToOne;
                $orToZero = $leftToZero + $rightToZero;
                $orToOne = min($leftToOne, $leftToZero + $rightToOne, $rightToZero + $leftToOne);
                $val = $andVal;
                $toZero = min($andToZero, 1 + $orToZero);
                $toOne = min($andToOne, 1 + $orToOne);
            } else {
                $orVal = $leftVal | $rightVal;
                $orToZero = $leftToZero + $rightToZero;
                $orToOne = min($leftToOne, $leftToZero + $rightToOne, $rightToZero + $leftToOne);
                $andToZero = min($leftToZero, $leftToOne + $rightToZero);
                $andToOne = $leftToOne + $rightToOne;
                $val = $orVal;
                $toZero = min($orToZero, 1 + $andToZero);
                $toOne = min($orToOne, 1 + $andToOne);
            }
            return [$val, $toZero, $toOne];
        };

        $index = 0;
        $parseFactor = null;
        $parseExpr = null;

        $parseFactor = function () use ($expression, &$index, &$parseExpr) {
            if ($expression[$index] === '0' || $expression[$index] === '1') {
                $value = (int)$expression[$index];
                $index++;
                $toZero = $value === 0 ? 0 : 1;
                $toOne = $value === 0 ? 1 : 0;
                return [$value, $toZero, $toOne];
            }
            $index++;
            $node = $parseExpr();
            $index++;
            return $node;
        };

        $parseExpr = function () use ($expression, &$index, $combine, &$parseFactor) {
            $node = $parseFactor();
            while ($index < strlen($expression) && ($expression[$index] === '&' || $expression[$index] === '|')) {
                $op = $expression[$index];
                $index++;
                $node = $combine($node, $op, $parseFactor());
            }
            return $node;
        };

        [$value, $toZero, $toOne] = $parseExpr();
        return $value ? $toZero : $toOne;
    }
}
