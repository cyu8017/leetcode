<?php
// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

class Solution {
    /**
     * @param String $s
     * @param Integer[] $shifts
     * @return String
     */
    function shiftingLetters($s, $shifts) {
        $arr = str_split($s);
        $total = 0;
        for ($i = count($arr) - 1; $i >= 0; $i--) {
            $total = ($total + $shifts[$i]) % 26;
            $arr[$i] = chr((ord($arr[$i]) - 97 + $total) % 26 + 97);
        }
        return implode('', $arr);
    }
}
