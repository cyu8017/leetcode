<?php
// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

class Solution {
    function maximumOddBinaryNumber($s) {
        $ones = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === '1') $ones++;
        $zeros = $n - $ones;
        return str_repeat('1', $ones - 1) . str_repeat('0', $zeros) . '1';
    }
}
