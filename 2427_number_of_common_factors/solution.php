<?php
// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

class Solution {
    function commonFactors($a, $b) {
        $gcd = function ($x, $y) {
            while ($y !== 0) {
                $t = $x % $y;
                $x = $y;
                $y = $t;
            }
            return $x;
        };
        $g = $gcd($a, $b);
        $ans = 0;
        for ($i = 1; $i * $i <= $g; $i++) {
            if ($g % $i === 0) {
                $ans++;
                if ($i * $i !== $g) $ans++;
            }
        }
        return $ans;
    }
}
