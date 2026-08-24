<?php
// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

class Solution {
    function evaluate($expression) {
        $tokens = [];
        $cur = '';
        $len = strlen($expression);
        for ($ti = 0; $ti < $len; $ti++) {
            $ch = $expression[$ti];
            if ($ch === '(' || $ch === ')') {
                if (strlen($cur) > 0) { $tokens[] = $cur; $cur = ''; }
                $tokens[] = $ch;
            } else if (preg_match('/\s/', $ch)) {
                if (strlen($cur) > 0) { $tokens[] = $cur; $cur = ''; }
            } else $cur .= $ch;
        }
        if (strlen($cur) > 0) $tokens[] = $cur;
        $pos = 0;
        $parse = function ($env) use (&$parse, &$tokens, &$pos) {
            $token = $tokens[$pos];
            if ($token !== '(') {
                $pos++;
                if (($token[0] >= '0' && $token[0] <= '9') || ($token[0] === '-' && strlen($token) > 1))
                    return intval($token, 10);
                for ($i = count($env) - 1; $i >= 0; $i--) {
                    if (array_key_exists($token, $env[$i])) return $env[$i][$token];
                }
                return 0;
            }
            $pos++;
            $op = $tokens[$pos++];
            if ($op === 'let') {
                $env[] = [];
                $ei = count($env) - 1;
                while ($tokens[$pos] !== ')') {
                    if ($tokens[$pos] === '(' || $tokens[$pos + 1] === ')') {
                        $value = $parse($env);
                        $pos++;
                        array_pop($env);
                        return $value;
                    }
                    $v = $tokens[$pos++];
                    $env[$ei][$v] = $parse($env);
                    $ei = count($env) - 1;
                }
            }
            if ($op === 'add') {
                $left = $parse($env);
                $right = $parse($env);
                $pos++;
                return $left + $right;
            }
            if ($op === 'mult') {
                $left = $parse($env);
                $right = $parse($env);
                $pos++;
                return $left * $right;
            }
            return 0;
        };
        return $parse([]);
    }
}
