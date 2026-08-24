<?php
// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

class Solution {
    function countOddLetters($n) {
        $d = ['zero','one','two','three','four','five','six','seven','eight','nine'];
        $mask = 0;
        while ($n > 0) {
            $word = $d[$n % 10];
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) $mask ^= 1 << (ord($word[$i]) - 97);
            $n = intdiv($n, 10);
        }
        $cnt = 0;
        while ($mask) { $cnt += $mask & 1; $mask >>= 1; }
        return $cnt;
    }
}
