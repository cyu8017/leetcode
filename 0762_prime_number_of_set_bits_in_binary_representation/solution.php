<?php
// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution {
    function countPrimeSetBits($left, $right) {
        $primes = [2 => true, 3 => true, 5 => true, 7 => true, 11 => true, 13 => true, 17 => true, 19 => true];
        $ans = 0;
        for ($num = $left; $num <= $right; $num++) {
            $bits = 0;
            $x = $num;
            while ($x > 0) { $bits += $x & 1; $x >>= 1; }
            if (isset($primes[$bits])) $ans++;
        }
        return $ans;
    }
}
