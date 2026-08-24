<?php
// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

class Solution {
    function subarrayGCD($nums, $k) {
        $gcd = function ($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $g = 0;
            for ($j = $i; $j < $n; $j++) {
                $g = $gcd($g, $nums[$j]);
                if ($g < $k) break;
                if ($g === $k) $ans++;
            }
        }
        return $ans;
    }
}
