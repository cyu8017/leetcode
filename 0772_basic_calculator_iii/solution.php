<?php
// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

class Solution {
    function calculate($s) {
        $expr = '';
        $slen = strlen($s);
        for ($si = 0; $si < $slen; $si++) if (!preg_match('/\s/', $s[$si])) $expr .= $s[$si];
        $i = 0;
        $parse = function () use (&$parse, &$expr, &$i) {
            $stack = [];
            $num = 0;
            $sign = '+';
            $elen = strlen($expr);
            while ($i < $elen) {
                $ch = $expr[$i];
                if ($ch >= '0' && $ch <= '9') $num = $num * 10 + (ord($ch) - 48);
                else if ($ch === '(') {
                    $i++;
                    $num = $parse();
                }
                if ((!($ch >= '0' && $ch <= '9') && $ch !== '(') || $i === $elen - 1) {
                    if ($ch === '+' || $ch === '-' || $ch === '*' || $ch === '/' || $ch === ')' || $i === $elen - 1) {
                        if ($sign === '+') $stack[] = $num;
                        else if ($sign === '-') $stack[] = -$num;
                        else if ($sign === '*') $stack[count($stack) - 1] *= $num;
                        else if ($sign === '/') {
                            $top = array_pop($stack);
                            $stack[] = (int)($top / $num);
                        }
                        if ($ch === ')') {
                            $sum = 0;
                            foreach ($stack as $v) $sum += $v;
                            return $sum;
                        }
                        $sign = $ch;
                        $num = 0;
                    }
                }
                $i++;
            }
            $total = 0;
            foreach ($stack as $v) $total += $v;
            return $total;
        };
        return $parse();
    }
}
