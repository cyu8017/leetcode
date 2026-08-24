<?php
// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

class Solution {
    function multiply($poly1, $poly2) {
        $n1 = count($poly1);
        $n2 = count($poly2);
        if ($n1 === 0 || $n2 === 0) return [];
        $m = $n1 + $n2 - 1;
        $res = array_fill(0, $m, 0);
        for ($i = 0; $i < $n1; $i++)
            for ($j = 0; $j < $n2; $j++)
                $res[$i + $j] += $poly1[$i] * $poly2[$j];
        return $res;
    }
}
