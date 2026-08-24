<?php
// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution {
    function removeDigit($number, $digit) {
        $best = '';
        $n = strlen($number);
        for ($i = 0; $i < $n; $i++) {
            if ($number[$i] === $digit) {
                $cand = substr($number, 0, $i) . substr($number, $i + 1);
                if ($cand > $best) $best = $cand;
            }
        }
        return $best;
    }
}
