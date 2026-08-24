<?php
// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

class Solution {
    function evaluateExpression($expression) {
        $parse = function($i) use (&$parse, $expression) {
            $ch = $expression[$i];
            if (($ch >= '0' && $ch <= '9') || $ch === '-') {
                $j = $i;
                if ($expression[$j] === '-') $j++;
                while ($j < strlen($expression) && $expression[$j] >= '0' && $expression[$j] <= '9') $j++;
                return [intval(substr($expression, $i, $j - $i)), $j];
            }
            $j = $i;
            while ($expression[$j] !== '(') $j++;
            $op = substr($expression, $i, $j - $i);
            $j++;
            $p1 = $parse($j);
            $j = $p1[1] + 1;
            $p2 = $parse($j);
            $j = $p2[1] + 1;
            $res = 0;
            if ($op === "add") $res = $p1[0] + $p2[0];
            else if ($op === "sub") $res = $p1[0] - $p2[0];
            else if ($op === "mul") $res = $p1[0] * $p2[0];
            else if ($op === "div") $res = intdiv($p1[0], $p2[0]);
            return [$res, $j];
        };
        return $parse(0)[0];
    }
}
