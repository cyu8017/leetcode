<?php

// LeetCode 0233 - Number of Digit One
// https://leetcode.com/problems/number-of-digit-one/

class Solution {
    function countDigitOne($n) {
        $count = 0;
        $factor = 1;
        while ($factor <= $n) {
            $lower = $n % $factor;
            $current = intdiv($n, $factor) % 10;
            $higher = intdiv($n, $factor * 10);
            if ($current === 0) {
                $count += $higher * $factor;
            } elseif ($current === 1) {
                $count += $higher * $factor + $lower + 1;
            } else {
                $count += ($higher + 1) * $factor;
            }
            $factor *= 10;
        }
        return $count;
    }
}
