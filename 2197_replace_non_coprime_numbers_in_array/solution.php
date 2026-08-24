<?php
// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

class Solution {
    function replaceNonCoprimes($nums) {
        $gcd = function($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $stack = [];
        foreach ($nums as $x0) {
            $x = $x0;
            while (count($stack) > 0) {
                $g = $gcd($stack[count($stack) - 1], $x);
                if ($g === 1) break;
                $x = intdiv($stack[count($stack) - 1], $g) * $x;
                array_pop($stack);
            }
            $stack[] = $x;
        }
        return $stack;
    }
}
