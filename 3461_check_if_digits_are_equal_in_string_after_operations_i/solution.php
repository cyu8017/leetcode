<?php
// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution {
    function hasSameDigits($s) {
        $b = str_split($s);
        while (count($b) > 2) {
            $nb = array_fill(0, count($b) - 1, "0");
            for ($i = 0; $i + 1 < count($b); $i++) {
                $nb[$i] = strval((ord($b[$i]) - 48 + ord($b[$i + 1]) - 48) % 10);
            }
            $b = $nb;
        }
        return $b[0] === $b[1];
    }
}
