<?php
// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minSwaps($s) {
        $zeros = substr_count($s, '0');
        $ones = strlen($s) - $zeros;
        if (abs($zeros - $ones) > 1) {
            return -1;
        }

        $mismatches = function (string $pattern) use ($s): int {
            $count = 0;
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                if ($s[$i] !== $pattern[$i % 2]) {
                    $count++;
                }
            }
            return intdiv($count, 2);
        };

        if ($zeros === $ones) {
            return min($mismatches('01'), $mismatches('10'));
        }
        if ($zeros > $ones) {
            return $mismatches('01');
        }
        return $mismatches('10');
    }
}
