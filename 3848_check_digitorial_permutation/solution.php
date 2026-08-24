<?php
// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

class Solution {
    function isDigitorialPermutation($n) {
        $f = array_fill(0, 10, 0);
        $f[0] = 1;
        for ($i = 1; $i < 10; $i++) $f[$i] = $f[$i - 1] * $i;
        $x = 0;
        $y = $n;
        while ($y > 0) {
            $x += $f[$y % 10];
            $y = intdiv($y, 10);
        }
        $a = str_split(strval($x));
        sort($a);
        $b = str_split(strval($n));
        sort($b);
        return implode('', $a) === implode('', $b);
    }
}
