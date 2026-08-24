<?php
// LeetCode 0065 - Valid Number
// https://leetcode.com/problems/valid-number/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function isNumber($s) {
        $seenDigit = false;
        $seenDot = false;
        $seenExp = false;
        $length = strlen($s);

        for ($i = 0; $i < $length; $i++) {
            $ch = $s[$i];

            if ($ch >= '0' && $ch <= '9') {
                $seenDigit = true;
            } elseif ($ch === '+' || $ch === '-') {
                if ($i > 0 && $s[$i - 1] !== 'e' && $s[$i - 1] !== 'E') {
                    return false;
                }
            } elseif ($ch === 'e' || $ch === 'E') {
                if ($seenExp || !$seenDigit) {
                    return false;
                }
                $seenExp = true;
                $seenDigit = false;
                $seenDot = false;
            } elseif ($ch === '.') {
                if ($seenDot || $seenExp) {
                    return false;
                }
                $seenDot = true;
            } else {
                return false;
            }
        }

        return $seenDigit;
    }
}
