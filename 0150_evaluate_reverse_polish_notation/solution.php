<?php

class Solution {
    function evalRPN(array $tokens): int {
        $stack = [];
        foreach ($tokens as $token) {
            if (in_array($token, ["+", "-", "*", "/"], true)) {
                $right = array_pop($stack);
                $left = array_pop($stack);
                switch ($token) {
                    case "+":
                        $stack[] = $left + $right;
                        break;
                    case "-":
                        $stack[] = $left - $right;
                        break;
                    case "*":
                        $stack[] = $left * $right;
                        break;
                    default:
                        $stack[] = intdiv($left, $right);
                }
            } else {
                $stack[] = (int) $token;
            }
        }
        return $stack[count($stack) - 1];
    }
}