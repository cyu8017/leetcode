<?php
// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function nextBeautifulNumber($n) {
        $balanced = function ($x) {
            $cnt = array_fill(0, 10, 0);
            while ($x > 0) { $cnt[$x % 10]++; $x = intdiv($x, 10); }
            for ($d = 0; $d < 10; $d++) if ($cnt[$d] !== 0 && $cnt[$d] !== $d) return false;
            return true;
        };
        for ($x = $n + 1; ; $x++) if ($balanced($x)) return $x;
    }
}
