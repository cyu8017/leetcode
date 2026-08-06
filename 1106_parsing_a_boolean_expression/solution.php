<?php
// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution {
    /**
     * @param String $expression
     * @return Boolean
     */
    function parseBoolExpr($expression) {
        $stack = [];
        $n = strlen($expression);
        for ($i = 0; $i < $n; $i++) {
            $ch = $expression[$i];
            if ($ch === ')') {
                $values = [];
                while (!empty($stack) && !in_array(end($stack), ['&', '|', '!'], true)) {
                    $token = array_pop($stack);
                    if ($token === 't' || $token === 'f') {
                        $values[] = $token === 't';
                    }
                }
                $op = array_pop($stack);
                if ($op === '!') {
                    $stack[] = !$values[0] ? 't' : 'f';
                } elseif ($op === '&') {
                    $stack[] = !in_array(false, $values, true) ? 't' : 'f';
                } else {
                    $stack[] = in_array(true, $values, true) ? 't' : 'f';
                }
            } elseif ($ch !== ',') {
                $stack[] = $ch;
            }
        }
        return end($stack) === 't';
    }
}
