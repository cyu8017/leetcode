<?php
// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

class Solution {
    function minimumCosts($regular, $express, $expressCost) {
        $n = count($regular);
        $ans = array_fill(0, $n, 0);
        $reg = 0;
        $exp = $expressCost;
        for ($i = 0; $i < $n; $i++) {
            $nextReg = min($reg + $regular[$i], $exp + $express[$i]);
            $nextExp = min($reg + $regular[$i] + $expressCost, $exp + $express[$i]);
            $reg = $nextReg;
            $exp = $nextExp;
            $ans[$i] = min($reg, $exp);
        }
        return $ans;
    }
}
