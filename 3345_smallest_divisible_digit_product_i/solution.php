<?php
// LeetCode 3345 - Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/

class Solution {
    function smallestNumber($n, $t) {
        for ($x = $n; ; $x++) {
            $p = 1;
            $y = $x;
            while ($y > 0) {
                $p *= $y % 10;
                $y = intdiv($y, 10);
            }
            if ($p % $t === 0) return $x;
        }
    }
}
