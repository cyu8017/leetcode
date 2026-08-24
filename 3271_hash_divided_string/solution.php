<?php
// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

class Solution {
    function stringHash($s, $k) {
        $out = '';
        $n = strlen($s);
        for ($i = 0; $i < $n; $i += $k) {
            $sum = 0;
            for ($j = $i; $j < $i + $k; $j++) $sum += ord($s[$j]) - 97;
            $out .= chr(97 + $sum % 26);
        }
        return $out;
    }
}
