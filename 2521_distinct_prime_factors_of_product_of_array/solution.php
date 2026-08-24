<?php
// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution {
    function distinctPrimeFactors($nums) {
        $set = [];
        foreach ($nums as $num) {
            $x = $num;
            for ($p = 2; $p * $p <= $x; $p++) {
                if ($x % $p === 0) {
                    $set[$p] = true;
                    while ($x % $p === 0) $x = intdiv($x, $p);
                }
            }
            if ($x > 1) $set[$x] = true;
        }
        return count($set);
    }
}
