<?php
// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

class Solution {
    function minimizeResult($expression) {
        $plus = strpos($expression, '+');
        $left = substr($expression, 0, $plus);
        $right = substr($expression, $plus + 1);
        $bestVal = PHP_INT_MAX;
        $best = '';
        for ($i = 0; $i < strlen($left); $i++) {
            for ($j = 1; $j <= strlen($right); $j++) {
                $a = substr($left, 0, $i);
                $b = substr($left, $i);
                $c = substr($right, 0, $j);
                $d = substr($right, $j);
                $val = intval($b) + intval($c);
                if (strlen($a)) $val *= intval($a);
                if (strlen($d)) $val *= intval($d);
                $cand = $a . '(' . $b . '+' . $c . ')' . $d;
                if ($val < $bestVal) { $bestVal = $val; $best = $cand; }
            }
        }
        return $best;
    }
}
