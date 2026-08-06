<?php
// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function maxAbsValExpr($arr1, $arr2) {
        $n = count($arr1);
        $ans = 0;
        $signs = [[1, 1], [1, -1], [-1, 1], [-1, -1]];
        foreach ($signs as [$a, $b]) {
            $mx = PHP_INT_MIN;
            $mn = PHP_INT_MAX;
            for ($i = 0; $i < $n; $i++) {
                $v = $a * $arr1[$i] + $b * $arr2[$i] + $i;
                $mx = max($mx, $v);
                $mn = min($mn, $v);
            }
            $ans = max($ans, $mx - $mn);
        }
        return $ans;
    }
}
