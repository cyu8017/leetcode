<?php
// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

class Solution {
    private function gcd($a, $b) {
        while ($b !== 0) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }

    function maxLength($nums) {
        $n = count($nums);
        $ans = 1;
        for ($i = 0; $i < $n; $i++) {
            $prod = 1;
            $g = 0;
            $l = 1;
            for ($j = $i; $j < $n; $j++) {
                if ($prod > intdiv(1000000000, $nums[$j])) break;
                $prod *= $nums[$j];
                if ($g === 0) {
                    $g = $nums[$j];
                    $l = $nums[$j];
                } else {
                    $g = $this->gcd($g, $nums[$j]);
                    $l = intdiv($l, $this->gcd($l, $nums[$j])) * $nums[$j];
                }
                if ($prod === $l * $g && $j - $i + 1 > $ans) $ans = $j - $i + 1;
            }
        }
        return $ans;
    }
}
