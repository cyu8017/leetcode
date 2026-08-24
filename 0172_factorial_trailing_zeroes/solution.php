<?php
// LeetCode 0172 - Factorial Trailing Zeroes
// https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution {
    function trailingZeroes(int $n): int {
        $count = 0;
        while ($n > 0) {
            $n = intdiv($n, 5);
            $count += $n;
        }
        return $count;
    }
}
