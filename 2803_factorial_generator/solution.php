<?php
// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

class Solution {
    function factorialGenerator($n) {
        $out = [];
        $cur = 1;
        if ($n === 0) return [1];
        for ($i = 1; $i <= $n; $i++) {
            $cur *= $i;
            $out[] = $cur;
        }
        return $out;
    }
}
