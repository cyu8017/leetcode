<?php
// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

class Solution {
    function oddString($words) {
        $diff = function ($w) {
            $b = '';
            $len = strlen($w);
            for ($i = 1; $i < $len; $i++) {
                $d = ord($w[$i]) - ord($w[$i - 1]);
                $b .= chr($d + 128) . ',';
            }
            return $b;
        };
        $d0 = $diff($words[0]);
        $d1 = $diff($words[1]);
        if ($d0 === $d1) {
            for ($i = 2; $i < count($words); $i++) {
                if ($diff($words[$i]) !== $d0) return $words[$i];
            }
        }
        if ($diff($words[2]) === $d0) return $words[1];
        return $words[0];
    }
}
